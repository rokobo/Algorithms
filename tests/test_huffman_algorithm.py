from huffman_codes import Huffman


def test_small_graph() -> None:
    graph = Huffman([42, 20, 5, 10, 11, 12, 24])
    _, min_code, max_code = graph.get_code_lengths()
    assert min_code == 2
    assert max_code == 4


def test_large_graph() -> None:
    with open("tests/LargeArrayHuffman.txt", "r") as file:
        graph = Huffman([int(i) for i in file])
    _, min_code, max_code = graph.get_code_lengths()
    assert min_code == 9
    assert max_code == 19
