"""Algorithm for computing minimum spanning tree."""
import sys
from typing import Union
from itertools import combinations

sys.setrecursionlimit(20000)


class UnionFind:
    """Union-find data structure for Kruskal's algorithm."""
    def __init__(
        self, graph: Union[list[tuple], list[str]]
    ) -> None:
        if not isinstance(graph, list):
            raise AttributeError
        if isinstance(graph[0], tuple):  # List of edges
            self.graph = sorted(graph, key=lambda x: x[0])
            self.edges = self.graph.copy()
            self.forests = {node: {node} for e in graph for node in e[1:]}
            self.forest_count = len(self.forests)
            self.mst = []
            self._type = 0
        elif isinstance(graph[0], int):  # Hamming distance matrix
            self.graph = graph
            self.bits = len(bin(max(graph))) - 2
            self.parent = {node: node for node in graph}
            self._type = 1
        else:
            raise AttributeError

    def _reset(self) -> None:
        if self._type == 0:  # List of edges
            self.forests = {node: {node} for e in self.graph for node in e[1:]}
            self.forest_count = len(self.forests)
            self.mst = []
        if self._type == 1:  # Hamming distance matrix
            self.parent = {node: node for node in self.graph}

    def _find(self, node: int) -> int:
        """
        Returns the leader vertex of a group that the node belongs to.

        Args:
            node (int): Node value.

        Returns:
            str: Leader vertex.
        """
        if self._type == 0:
            for leader, forest in self.forests.items():
                if node in forest:
                    return leader
        else:
            if self.parent[node] == node:
                return node

            # Path compression
            if self.parent[node] != node:
                self.parent[node] = self._find(self.parent[node])

            return self._find(self.parent[node])
        raise ValueError

    def _union(self, l1: int, l2: int) -> None:
        """
        Fuses two forests into a single one.

        Args:
            l1 (int): Leader vertex one.
            l2 (int): Leader vertex two.
        """
        if self._type == 0:
            self.forests[l1] = self.forests[l1] | (self.forests[l2])
            del self.forests[l2]
            self.forest_count -= 1
        else:
            self.parent[l1] = l2

    def kruskal(
        self, clusters: int = 1
    ) -> tuple[dict[int, set[int]], list[tuple]]:
        """
        Kruskal's algorithm for clustering application.

        Args:
            clusters (int): Number of forests (clusters). Defaults to 1.

        Returns:
            tuple[dict[int, set[int]], list[tuple[int, int, int]]]:
                Forest groups and edge list.
        """
        if self._type != 0:
            raise TypeError("Method not available for given type")
        self._reset()
        for edge_cost, node1, node2 in self.graph:
            if self.forest_count == clusters:
                break
            forest1 = self._find(node1)
            forest2 = self._find(node2)

            if forest1 != forest2:
                self._union(forest1, forest2)
                self.mst.append((edge_cost, node1, node2))

        else:
            raise SystemError
        return self.forests, self.mst

    def find_cluster_max_spacing(
        self, clusters: int
    ) -> tuple[dict[int, set[int]], list[tuple], int]:
        """
        Finds max spacing after applying clustering algorithm using kruskal's.

        Args:
            clusters (int): Number of clusters.

        Returns:
            tuple[dict[int, set[int]], list[tuple], int]:
                Forest groups, edge list, max spacing.
        """
        if self._type != 0:
            raise TypeError("Method not available for given type")
        forest, mst = self.kruskal(clusters)
        graph = sorted(self.graph.copy(), key=lambda x: x[0], reverse=True)

        # Remove edges from clusters
        for edge in mst:
            graph.remove(edge)

        # Find max spacing between all clusters using the remaining edges
        max_spacing = float("inf")
        for edge, node1, node2 in graph:
            if self._find(node1) != self._find(node2):
                if edge < max_spacing:
                    max_spacing = edge
        return forest, mst, max_spacing

    def find_max_cluster_spacing(
        self, spacing: int
    ) -> tuple[dict[int, set[int]], list[tuple], int]:
        """
        Finds the max number of clusters for the given spacing.

        Args:
            spacing (int): Max spacing.

        Returns:
            tuple[dict[int, set[int]], list[tuple], int]: _description_
        """
        if self._type != 1:
            raise TypeError("Method not available for given type")
        self._reset()

        # Eliminate duplicates (forests already account for this)
        graph = list(set(self.graph.copy()))
        nodes = set(graph)  # Speed up lookup

        # Make bit masks for all possible distance masks.
        bit_masks = [
            sum(1 << i for i in bits)
            for distance in range(1, spacing + 1)
            for bits in combinations(range(self.bits), distance)
        ]

        for bit_mask in bit_masks:
            for node in graph:
                node2 = node ^ bit_mask
                if node2 not in nodes:
                    continue
                forest1 = self._find(node)
                forest2 = self._find(node2)
                if forest1 != forest2:
                    self._union(forest1, forest2)
        return len(set(self._find(i) for i in graph))
