from kruskal_algorithm import UnionFind


def test_small_edge_list() -> None:
    graph = UnionFind([(10, 1, 5), (5, 5, 3), (4, 4, 5),
        (3, 1, 4), (2, 4, 3), (1, 3, 2), (1, 5, 1)])

    assert graph.kruskal()[1] == [(1, 3, 2), (1, 5, 1), (2, 4, 3), (3, 1, 4)]

    forests, mst, max_spacing = graph.find_cluster_max_spacing(3)
    assert forests == {3: {2, 3}, 5: {1, 5}, 4: {4}}
    assert mst == [(1, 3, 2), (1, 5, 1)]
    assert max_spacing == 2


def test_small_matrix() -> None:
    graph = UnionFind([51, 35, 0, 1])
    assert graph.find_max_cluster_spacing(1) == 2
    assert graph.find_max_cluster_spacing(2) == 1
    assert graph.find_max_cluster_spacing(3) == 1
    graph = UnionFind([63, 63, 62, 0])
    assert graph.find_max_cluster_spacing(1) == 2
    assert graph.find_max_cluster_spacing(2) == 2
    graph = UnionFind([63, 63, 63, 0])
    assert graph.find_max_cluster_spacing(1) == 2
    assert graph.find_max_cluster_spacing(2) == 2



def test_large_edge_list() -> None:
    with open("tests/LargeArrayClustering.txt", "r") as file:
        graph = UnionFind([
            (int(c), int(n1), int(n2))
            for edge in file
            for n1, n2, c in [edge.split()]
        ])

    _, _, max_spacing = graph.find_cluster_max_spacing(4)
    assert max_spacing == 106


def test_large_matrix() -> None:
    with open("tests/LargeArrayClustering2.txt", "r") as file:
        graph = UnionFind([int(''.join(num.split()), 2) for num in file])

    assert graph.find_max_cluster_spacing(2) == 6118
