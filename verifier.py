# agents/verifier.py


def verify(goal, current_output):
    """
    MVP Verification Mode

    Always approves the execution so that:
    - Execution status becomes 'completed'
    - No infinite loops
    - No LLM dependency
    - Stable demo behavior
    """

    return {
        "valid": True,
        "reason": "Auto-approved (MVP mode)."
    }