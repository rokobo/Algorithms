from math import log
from time import perf_counter
from copy import deepcopy
from random import choice
from multiprocessing import cpu_count, Pool


def random_contraction_algorithm(original_graph: list[list[int]]) -> int:
    """
    Contracts the graph until only two nodes exist.

    Args:
        original_graph list[list[int]]: Adjancency dict.

    Returns:
        int: minimum cut found.
    """
    graph = deepcopy(original_graph)
    unique_elements = set(item[0] for item in graph)
    while len(unique_elements) > 2:
        # Choose an edge
        node, edge = choice(graph)
        unique_elements.discard(edge)

        # remove [node, edge] and [edge, node]
        if [node, edge] in graph:
            graph.remove([node, edge])
            graph.remove([edge, node])

        # Merge nodes
        for i in graph:
            if i[0] == edge:
                i[0] = node
            if i[1] == edge:
                i[1] = node

        # Remove self-loops
        graph = [x for x in graph if x[0] != x[1]]
    return len(graph)/2


def verify_graph(graph: list[list[int]]):
    assert len(graph) % 2 == 0
    for edge in graph:
        assert [edge[1], edge[0]] in graph


def minimum_cut(original_graph: list[list[int]], trials: int = None) -> int:
    """
    Performs the randomized contraction algorithm multiple times.

    Args:
        original_graph list[list[int]]: Adjancency list.
        trials (int): override the number of algorithm trials.

    Returns:
        int: Number of edges of minimum cut
    """
    verify_graph(original_graph)
    start = perf_counter()
    size = len(original_graph)
    if trials is None:
        trials = int(size**2 * log(size))

    # Multiprocessing
    with Pool(processes=cpu_count()) as pool:
        results = list(pool.imap_unordered(
            random_contraction_algorithm,
            [original_graph] * trials,
            chunksize=1
        ))
    end = perf_counter()

    print(f'Minimum cut is: {min(results)}')
    print(f'Did {trials} trials')
    print(f'Finished in {round(end - start, 1)} seconds')
    return min(results)


if __name__ == '__main__':
    large_graph = []
    with open('../tests/LargeArrayMinCut.txt', 'r') as file:
        for line in file:
            values = line.strip().split()
            current_node = int(values[0])
            edge_list = list(map(int, values[1:]))
            for current_edge in edge_list:
                large_graph.append([current_node, current_edge])

    minimum_cut(large_graph, 800)
