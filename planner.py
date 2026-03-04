# agents/planner.py

from core.llm import call_llm


def plan(goal):
    """
    Planning Agent:
    Converts high-level goal into structured execution steps.
    Does NOT rely on strict JSON from the model.
    """

    system_prompt = """
You are a strategic planning agent.

Generate a clear numbered list of execution steps.
Do NOT use markdown formatting.
Do NOT include headings.
Only return plain numbered steps like:

1. Step one
2. Step two
3. Step three
"""

    user_prompt = f"Goal: {goal.outcome}"

    raw_output = call_llm(system_prompt, user_prompt)

    # --- Parse numbered steps safely ---
    lines = raw_output.split("\n")
    steps = []

    for line in lines:
        line = line.strip()

        # Accept lines that start with a number
        if line and line[0].isdigit():
            # Remove "1. ", "2) ", etc.
            step = line.split(".", 1)[-1].strip()
            steps.append(step)

    # Fallback if model ignores numbering
    if not steps:
        steps = [raw_output.strip()]

    return {
        "plan": steps,
        "risk_assessment": "Auto-generated plan. Validate feasibility."
    }