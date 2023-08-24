from dijkstra_algorithm import dijkstra_algorithm


def test_large_array() -> None:
    graph = {}
    with open('tests/LargeArrayDijkstra.txt', 'r') as file:
        for line in file:
            elements = line.strip().split()
            node = int(elements[0])
            edges = [tuple(map(int, edge.split(','))) for edge in elements[1:]]
            graph[node] = edges
    destinations = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    correct = [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]
    results = []
    for destination in destinations:
        results.append(dijkstra_algorithm(graph, destination))
    assert results == correct
