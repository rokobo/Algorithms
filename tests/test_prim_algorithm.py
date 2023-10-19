from prim_algorithm import prim_algorithm


def test_small_graph() -> None:
    assert prim_algorithm([(2, 1, 2), (3, 2, 3)]) == 5
    assert prim_algorithm([(2, 1, 2), (3, 1, 4), (-2, 2, 4)]) == 0
    graph = [(9, 1, 4), (10, 1, 5), (5, 5, 3),
        (4, 4, 5), (3, 1, 4), (2, 4, 3), (1, 3, 2)]
    assert prim_algorithm(graph) == 10


def test_large_graph() -> None:
    with open("tests/LargeArrayPrim.txt", "r") as file:
        graph = [
            (int(c), int(n1), int(n2))
            for edge in file
            for n1, n2, c in [edge.split()]
        ]
    assert prim_algorithm(graph) == -3612829
