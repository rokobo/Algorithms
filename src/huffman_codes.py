"""Algorithms for Huffman codes."""
import heapq


class Huffman:
    """Class for Huffman code methods."""
    def __init__(self, weights: list[int]) -> None:
        self._weights = weights
        self._build_codes()

    def _build_codes(self) -> None:
        """
        Generates Huffman codes.
        """
        self._heap = [(w, [i]) for i, w in enumerate(self._weights)]
        heapq.heapify(self._heap)
        self._tree = self._heap.copy()

        while len(self._heap) > 1:
            node1 = heapq.heappop(self._heap)
            node2 = heapq.heappop(self._heap)
            new_node = (node1[0] + node2[0], [node1[1], node2[1]])
            heapq.heappush(self._heap, new_node)
            heapq.heappush(self._tree, new_node)
        self._codes = dict()
        self._traverse(self._tree.pop())

    def _find(self, values: list[list, list]) -> list[int, int]:
        """
        Function for finding indexes of values in self._tree.

        Args:
            values (list[list, list]): Values.

        Returns:
            list[int, int]: Indexes.
        """
        indexes = []
        for i, val in enumerate(self._tree):
            if val[1] in values:
                indexes.append(i)
            if len(indexes) == len(values):
                break
        return indexes

    def _traverse(self, node: tuple, code: str = ""):
        """
        Recursive function to traverse the tree produced by _build_codes
        and build a code dictionary.

        Args:
            node (tuple): Current node of the traversal.
            code (str, optional): Current code string in path. Defaults to "".
        """
        if len(node[1]) != 1:
            left_index, right_index = self._find(node[1])
            self._traverse(self._tree[left_index], code + "0")
            self._traverse(self._tree[right_index], code + "1")
        else:
            self._codes[node[0]] = code

    def get_codes(self) -> dict[int, str]:
        """
        Returns the Huffman codes dictionary.

        Returns:
            dict[int, str]: Index of the symbol and code string.
        """
        return self._codes

    def get_code_lengths(self) -> tuple[list[int], int, int]:
        """
        Returns code information related to the length of the codes.

        Returns:
            tuple[list[int], int, int]:
                List of code lengths, minimum length, max length.
        """
        lengths = [len(code) for code in self._codes.values()]
        return lengths, min(lengths), max(lengths)
