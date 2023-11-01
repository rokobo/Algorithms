from wis_algorithm import WIS


def test_small_graph() -> None:
    graph = WIS([5])
    assert graph.get_wis() == 5
    assert graph.get_nodes() == [0]

    graph = WIS([3, 4])
    assert graph.get_wis() == 4
    assert graph.get_nodes() == [1]

    graph = WIS([7, 1, 7, 10])
    assert graph.get_wis() == 17
    assert graph.get_nodes() == [0, 3]

    graph = WIS([3, 4, 3, 1, 0, 10])
    assert graph.get_wis() == 16
    assert graph.get_nodes() == [0, 2, 5]


def test_medium_graph() -> None:
    graph = WIS([10, 460, 250, 730, 63, 379, 638, 122, 435, 705, 84])
    assert graph.get_wis() == 2533
    assert graph.get_nodes() == [1, 3, 6, 9]

    graph = WIS([10, 280, 618, 762, 908, 409, 34, 59, 277, 246, 779])
    assert graph.get_wis() == 2626
    assert graph.get_nodes() == [0, 2, 4, 6, 8, 10]

    graph = WIS([10, 280, 618, 762, 908, 409, 34, 312, 277, 246, 779])
    assert graph.get_wis() == 2627
    assert graph.get_nodes() == [0, 2, 4, 7, 10]


def test_large_graph() -> None:
    with open("tests/LargeArrayWIS.txt", "r") as file:
        graph = WIS([int(i) for i in file])

    assert graph.get_wis() == 2955353732
    node_results = graph.get_nodes()
    nodes = [0, 1, 2, 3, 16, 116, 516, 996]
    expected = [True, False, True, False, False, True, True, False]
    assert [node in node_results for node in nodes] == expected
