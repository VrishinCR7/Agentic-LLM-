def evaluate_progress(output: str, goal) -> float:
    """
    Simple bounded progress heuristic for MVP.
    Replace later with distance-based function.
    """

    if not output:
        return 0.0

    goal_length = max(len(goal.outcome), 1)
    score = min(len(output) / goal_length, 1.0)

    return round(score, 3)