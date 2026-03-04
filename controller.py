from agents.planner import plan
from agents.executor import execute
from agents.verifier import verify
from policies.redirection import redirect
from core.progress import evaluate_progress


def run_agent(goal):

    trace = []

    # --- Planning ---
    planning_output = plan(goal)
    steps = planning_output["plan"]

    trace.append({"stage": "planning", "data": steps})

    final_output = ""

    # --- Execution Loop ---
    while goal.invariant_valid():

        goal.iterations += 1

        for step in steps:
            execution = execute(step)

            # execution is now TEXT, not dict
            final_output += "\n" + str(execution)

        # --- Verification ---
        verification = verify(goal, final_output)

        trace.append({
            "stage": "verification",
            "valid": verification.get("valid", False),
            "reason": verification.get("reason", "Unknown")
        })

        if verification.get("valid", False):
            goal.progress = evaluate_progress(final_output, goal)

            return {
                "status": "completed",
                "output": final_output.strip(),
                "progress": goal.progress,
                "trace": trace
            }

        # --- Redirection ---
        redirection = redirect(goal, verification.get("reason", ""))

        # redirection may return text or dict depending on your implementation
        if isinstance(redirection, dict):
            steps = redirection.get("revised_plan", steps)

            trace.append({
                "stage": "redirection",
                "new_plan": steps
            })
        else:
            # If redirection returns plain text, keep existing steps
            trace.append({
                "stage": "redirection",
                "note": "Redirection returned text, plan unchanged."
            })

    # --- If Loop Exits ---
    return {
        "status": "failed",
        "output": final_output.strip(),
        "progress": goal.progress,
        "trace": trace
    }