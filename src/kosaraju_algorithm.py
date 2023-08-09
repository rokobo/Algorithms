"""Functions for computing strongly connected components (SCCs)."""
import sys
import threading
from collections import defaultdict
sys.setrecursionlimit(8000000)
threading.stack_size(67108864)


def dfs(graph, vertex, visited, stack):
    """
    Depth first search algorithm to find finishing times of a graph starting
    from the initial vertex passed.

    Args:
        graph (list[list[list]]): Adjacency list representing graph.
        initial_vertex (int): Vertex to start the DFS algorithm.
        return_len (bool): Function should return length and initial_vertex.

    Returns:
        list[int]: Finishing time.
    """
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)

    stack.append(vertex)


def reverse_graph(graph: dict[list[int]]) -> defaultdict[list[int]]:
    """
    Reverses the graph.

    Args:
        graph (dict[list[int]]): Adjacency list representing graph.

    Returns:
        defaultdict[list[int]]: Reversed graph.
    """
    reversed_graph = defaultdict(list)
    for i, nodes in graph.items():
        for node in nodes:
            if node not in reversed_graph:
                reversed_graph[node] = []
            reversed_graph[node].append(i)
        if i not in reversed_graph:
            reversed_graph[i] = []
    return reversed_graph


def main(graph):
    """
    Function used for thread call.

    Args:
        graph (dict): Graph.

    Returns:
        list[int]: Largest SCCs.
    """
    length = 1 + max(
        max(graph.keys()),
        max([node for nodes in graph.values() for node in nodes])
    )
    visited = [False] * length
    stack = []
    graph = defaultdict(list, graph)

    for vertex in list(graph.keys()):
        if not visited[vertex]:
            dfs(graph, vertex, visited, stack)

    reversed_graph = reverse_graph(graph)
    visited = [False] * length
    scc = []

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            scc_component = []
            dfs(reversed_graph, vertex, visited, scc_component)
            scc.append(scc_component)

    scc = sorted(scc, key=len, reverse=True)[:5]
    scc.extend([set()] * (5 - len(scc)))
    size = [len(x) for x in scc]
    global result
    result = size
    return size


def kosaraju_algorithm(graph: dict) -> list[int]:
    """
    Wrapper function for kosaraju algorithm.
    Uses another thread for stack overflow issues.

    Args:
        graph (dict): Graph.

    Returns:
        list[int]: Largest SCCs.
    """

    thread = threading.Thread(target=main, args=(graph,))
    thread.start()
    thread.join()
    return result
