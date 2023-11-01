"""Knapsack problem."""


def max_value_for_weight(items: list[tuple[int, int]], weight: int) -> int:
    """
    Returns the max value for a given max weight.

    Args:
        items (list[tuple[int, int]]): Items list, (value, weight).
        weight (int): Max weight.

    Returns:
        int: Max value.
    """
    # Only use the 2 most recent rows for saving memory
    row1 = [0 for _ in range(weight + 1)]
    row2 = row1.copy()

    for i in range(1, len(items) + 1):
        v, w = items[i - 1]
        for x in range(1, weight + 1):
            v1 = row1[x]
            if w > x:  # Too heavy case
                row2[x] = v1
            else:
                value = max(v1, row1[x - w] + v)
                row2[x] = value
        row1 = row2.copy()
    return row2[-1]
