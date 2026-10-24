"""Self-Correcting Code Patch & Stacktrace Repair.
100% Python Standard Library.
"""

import re

class StacktraceSelfRepairEngine:
    """Parses Python exception tracebacks and synthesizes minimal boundary check patches."""

    @staticmethod
    def diagnose_and_suggest_patch(error_type: str, error_message: str, code_snippet: str = "") -> dict:
        patches = []
        if error_type == "ZeroDivisionError":
            patches.append({
                "rule": "GUARD_ZERO_DENOMINATOR",
                "remediation": "Add 'if denominator == 0: return 0.0' or raise custom ValueError before division."
            })
        elif error_type == "KeyError":
            key_match = re.search(r"['\"](.*?)['\"]", error_message)
            key_name = key_match.group(1) if key_match else "key"
            patches.append({
                "rule": "DICT_GET_FALLBACK",
                "remediation": f"Replace direct subscript access with dictionary '.get(\"{key_name}\", default_value)'."
            })
        elif error_type == "IndexError":
            patches.append({
                "rule": "BOUNDS_CHECK",
                "remediation": "Check 'if len(sequence) > index:' before indexing into array."
            })
        else:
            patches.append({
                "rule": "GENERIC_EXCEPTION_CATCH",
                "remediation": "Wrap vulnerable block in specific try-except and log sanitized error."
            })

        return {
            "error_type": error_type,
            "error_message": error_message,
            "suggested_patches": patches,
            "patch_count": len(patches)
        }
