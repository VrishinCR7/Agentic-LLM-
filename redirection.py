from core.llm import call_llm


def redirect(goal, failure_reason):

    system_prompt = """
    You are a recovery agent.

    Given failure feedback, revise the plan.

    Output JSON:
    {
        "revised_plan": ["step1", "step2"]
    }
    """

    user_prompt = f"""
    Goal: {goal.outcome}
    Failure reason: {failure_reason}
    """

    return call_llm(system_prompt, user_prompt)