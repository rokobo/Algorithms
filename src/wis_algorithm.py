"""Weighted independent set problem algorithms."""


class WIS:
    """Weighted independent set solver."""
    def __init__(self, graph: list[int]):
        assert len(graph) != 0, "Graph cannot be empty"
        self.graph = graph
        self.solution = None

    def get_wis(self) -> int:
        """
        Solves the WIS problem and returns the max WIS's weight.

        Returns:
            int: Weight value.
        """
        if self.solution is not None:
            return self.solution[-1]

        self.solution = [0, self.graph[0]] + ([None] * (len(self.graph) - 1))
        for i in range(2, len(self.graph) + 1):
            self.solution[i] = max(
                self.solution[i-1],
                self.solution[i-2] + self.graph[i-1]
            )
        self.solution = self.solution[1:]
        return self.solution[-1]

    def get_nodes(self) -> list[int]:
        """
        Returns the WIS nodes using the internal solution array.

        Returns:
            list[int]: Node indexes of the optimal solution.
        """
        if self.solution is None:
            self.get_wis()

        if len(self.solution) < 3:
            return [self.solution.index(max(self.solution))]

        i = len(self.solution) - 1
        nodes = []

        while i > 1:
            if self.solution[i - 1] <= self.solution[i - 2] + self.graph[i]:
                nodes.append(i)
                i -= 2
            else:
                i -= 1

        if nodes[-1] != 2:
            nodes.append(1 if self.graph[1] > self.graph[0] else 0)
        else:
            nodes.append(0)
        return nodes[::-1]
