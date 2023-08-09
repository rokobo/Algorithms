from kosaraju_algorithm import reverse_graph, kosaraju_algorithm


def test_reverse_graph() -> None:
    graph = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}
    reversed_graph = reverse_graph(graph)
    assert reversed_graph == {0: [1], 1: [2], 2: [0], 3: [0], 4: [3]}


def test_kosaraju() -> None:
    result = kosaraju_algorithm(
        {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []})
    assert result == [3, 1, 1, 0, 0]

    result = kosaraju_algorithm({1: [2, 4], 4: [2], 3: [2, 4]})
    assert result == [1, 1, 1, 1, 0]

    result = kosaraju_algorithm({
        1: [4], 2: [8], 3: [6], 4: [7], 5: [2],
        6: [9], 7: [1], 8: [5, 6], 9: [7, 3]})
    assert result == [3, 3, 3, 0, 0]

    result = kosaraju_algorithm({
        1: [2], 2: [6, 3, 4], 3: [1, 4], 4: [5],
        5: [4], 6: [5, 7], 7: [6, 8], 8: [5, 7]})
    assert result == [3, 3, 2, 0, 0]

    result = kosaraju_algorithm({
        1: [2], 2: [3], 3: [1, 4],
        5: [4], 6: [4, 7], 8: [6], 7: [8]})
    assert result == [3, 3, 1, 1, 0]

    result = kosaraju_algorithm({
        1: [2], 2: [3], 3: [1, 4], 5: [4],
        6: [4, 7], 8: [6], 7: [8], 4: [3, 6]})
    assert result == [7, 1, 0, 0, 0]

    result = kosaraju_algorithm({
        1: [2], 2: [3, 4, 5], 3: [6], 4: [5, 7], 5: [2, 6, 7], 6: [3, 8],
        7: [8, 10], 8: [7], 9: [7], 10: [9, 11], 11: [12], 12: [10]})
    assert result == [6, 3, 2, 1, 0]


def test_large_array() -> None:
    with open('tests/LargeArraySCC.txt', 'r') as file:
        values = file.read()

    graph = {}
    for i, v in zip(*[iter(values.split())]*2):
        index, vertices = int(i), int(v)
        if index not in graph:
            graph[index] = []
        graph[index].append(vertices)
    result = kosaraju_algorithm(graph)
    assert result == [434821, 968, 459, 313, 211]
