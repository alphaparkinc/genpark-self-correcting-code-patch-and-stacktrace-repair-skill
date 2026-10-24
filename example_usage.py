"""Example usage for Stacktrace Self-Repair Engine."""
from client import StacktraceSelfRepairEngine

if __name__ == "__main__":
    res = StacktraceSelfRepairEngine.diagnose_and_suggest_patch("KeyError", "'auth_token'")
    print("Suggested Patch:", res["suggested_patches"])
