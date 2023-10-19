"""Algorithm for computing minimum spanning tree."""
import heapq


def prim_algorithm(edges: list[tuple[int, int, int]]) -> int:
    """
    Computes the cost of the minimum spanning tree using Prim's algorithm.

    Args:
        edges (list[tuple[int, int, int]]): Node1, node2, edge cost.

    Returns:
        int: Tree cost.
    """
    vertex = edges[0][1]
    not_connected = {node for edge in edges for node in edge[1:]}
    impossible_edges = set(edges)

    heap = [edge for edge in impossible_edges if vertex in edge[1:]]
    heapq.heapify(heap)
    starting_edge = heapq.heappop(heap)
    heapq.heappush(heap, starting_edge)
    graph = set()
    impossible_edges.discard(starting_edge)

    while not_connected and heap:
        # Get smallest weighted edge for connecting MST with remaining nodes
        smallest_edge = heapq.heappop(heap)
        if not bool(set(smallest_edge[1:]) & not_connected):
            continue
        if smallest_edge in graph:
            continue
        graph.add(smallest_edge)

        # Mark nodes as not_connected
        not_connected.discard(smallest_edge[1])
        not_connected.discard(smallest_edge[2])
        deletions = []
        # Update heap of available edges for choosing smallest edge
        for edge in impossible_edges:
            if any(node in edge[1:] for node in smallest_edge[1:]):
                heapq.heappush(heap, edge)
                deletions.append(edge)

        # Delete edges that were added to heap from edge list
        for edge in deletions:
            impossible_edges.discard(edge)

    # Determine final graph's cost
    cost = sum(edge[0] for edge in graph)
    return cost
