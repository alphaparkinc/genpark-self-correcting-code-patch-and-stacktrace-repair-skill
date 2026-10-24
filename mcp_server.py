"""MCP server for Stacktrace Self-Repair Engine."""
import sys
import json
from client import StacktraceSelfRepairEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "diagnose_stacktrace_patch",
                "description": "Synthesizes minimal defensive remediation patch for a runtime exception",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "error_type": {"type": "string"},
                        "error_message": {"type": "string"},
                        "code_snippet": {"type": "string"}
                    },
                    "required": ["error_type", "error_message"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "diagnose_stacktrace_patch":
            args = params.get("arguments", {})
            res = StacktraceSelfRepairEngine.diagnose_and_suggest_patch(
                args.get("error_type", ""),
                args.get("error_message", ""),
                args.get("code_snippet", "")
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
