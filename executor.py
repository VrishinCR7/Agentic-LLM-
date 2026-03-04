from core.llm import call_llm


def execute(step):

    system_prompt = """
    You are an execution agent.

Produce structured startup blueprint output:

Sections:
1. Problem
2. Target Users
3. Solution
4. Core Features
5. Tech Stack
6. Monetization
7. Go-to-Market

Return clean markdown.
    """

    user_prompt = f"Execute this step:\n{step}"

    return call_llm(system_prompt, user_prompt)