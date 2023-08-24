"""Functions for computing shortest path to destination."""


def dijkstra_algorithm(graph: dict[int, tuple[int]], destination: int) -> int:
    """
    Wrapper function for dijkstra algorithm.
    Node 1 is considered source.
    If no path is found, shortest path will return 1000000.

    Args:
        graph (dict[int, tuple[int]]): Graph with node: (edge, edge length).
        destination (int): Destination node.

    Returns:
        int: Shortest path length.
    """
    # Initialize tentative distances, unvisited set and iteration queue
    nodes = graph.keys()
    unvisited_nodes = set(nodes)
    node_distances = {node: float('inf') for node in nodes}
    node_distances[1] = 0

    # Main iteration
    while True:
        possible_nodes = [
            node for node in graph.keys() if node in unvisited_nodes
        ]
        if possible_nodes == []:
            break
        node = min(
            possible_nodes,
            key=lambda x: node_distances[x]
        )
        unvisited_nodes.remove(node)

        # Calculate tentative distance for node neighbors
        for neighbor in graph[node]:
            edge, distance = neighbor
            if edge not in unvisited_nodes:
                continue

            # If tentative distance is smaller, then recorded, update it
            tentative_distance = node_distances[node] + distance
            current_distance = node_distances[edge]
            if current_distance > tentative_distance:
                node_distances[edge] = tentative_distance

    # See if there is a path to destination node
    distance_to_destination = node_distances[destination]
    if distance_to_destination == float("inf"):
        return 1000000
    return distance_to_destination
