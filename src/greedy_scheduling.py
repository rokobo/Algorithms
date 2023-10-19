"""Algorithm for computing minimal weighted sum of job completion times."""


def scheduling_by_diff(jobs: list[tuple[int, int]]) -> int:
    """
    Scheduling algorithm that uses the weight - duration to sort order of jobs.
    (wrapper)

    Args:
        jobs (list[tuple[int, int]]): Jobs in the form of (weight, duration).

    Returns:
        int: Sum of weighted completion times.
    """
    sorted_jobs = sorted(jobs, key=lambda x: (x[0] - x[1], x[0]), reverse=True)
    return scheduling(sorted_jobs)


def scheduling_by_div(jobs: list[tuple[int, int]]) -> int:
    """
    Scheduling algorithm that uses the weight / duration to sort order of jobs.
    (wrapper)

    Args:
        jobs (list[tuple[int, int]]): Jobs in the form of (weight, duration).

    Returns:
        int: Sum of weighted completion times.
    """
    sorted_jobs = sorted(jobs, key=lambda x: (x[0] / x[1], x[0]), reverse=True)
    return scheduling(sorted_jobs)


def scheduling(jobs: list[tuple[int, int]]) -> int:
    """
    Scheduling algorithm backend.

    Args:
        jobs (list[tuple[int, int]]): Jobs in the form of (weight, duration).

    Returns:
        int: Sum of weighted completion times.
    """
    weighted_sum = 0
    completion_time = 0
    for w, d in jobs:
        completion_time += d
        weighted_sum += w * completion_time
    return weighted_sum
