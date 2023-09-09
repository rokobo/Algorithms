"""Functions for a 2-Sum algorithm."""
from multiprocessing import Pool, cpu_count


def find_sums_in_interval(
        hash_table: set[int], start: int,
        end: int) -> dict[int, tuple[int, int]]:
    """
    Finds all values in range(start, end + 1) that satisfy the 2-Sum problem.

    Args:
        hash_table (set[int]): Values.
        start (int): Start of range.
        end (int): End of range.

    Returns:
        dict[int, tuple[int, int]]: Results.
            The key is the target and the value is the 2-Sum solution.
    """
    hits = {var: False for var in range(start, end + 1)}
    targets = set(range(start, end + 1))

    for node in hash_table:
        for target in targets:
            lookup = target - node
            if node != lookup and lookup in hash_table:
                hits[target] = (max(node, lookup), min(node, lookup))
                targets.remove(target)
                break
    return hits


def solve_2_sum(
        hash_table: set[int], start: int,
        end: int) -> dict[int, tuple[int, int]]:
    """
    Wrapper function for using multiprocessing with find_sums_in_interval.

    Args:
        hash_table (set[int]): Values.
        start (int): Start of range.
        end (int): End of range.

    Returns:
        dict[int, tuple[int, int]]: Results.
            The key is the target and the value is the 2-Sum solution.
    """
    num_processes = cpu_count()
    if (end - start) > num_processes:
        chunk_size = (end - start) // num_processes
        args_list = [
            [hash_table, i, i + chunk_size]
            for i in range(start, end, chunk_size)
        ]
        args_list[-1][2] = end
        with Pool(processes=cpu_count()) as pool:
            results = pool.starmap(find_sums_in_interval, args_list)
        return sum(sum(bool(x) for x in r.values()) for r in results)

    result = find_sums_in_interval(hash_table, start, end)
    return sum(bool(x) for x in result.values())
