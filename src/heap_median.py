"""Functions for a median maintenance heap."""
from math import log2, floor, log
import random


# Define heap class
class Heap:
    """Heap class for extract-min and extract-max heaps."""
    def __init__(self, heap_type: str):
        self.heap = []
        if heap_type not in ["min", "max"]:
            raise ValueError("Argument must be min or max")
        self.heap_type = heap_type
        self.heap_size = 0

    def size(self) -> int:
        """
        Returns the size of the heap.

        Returns:
            int: Size of the heap.
        """
        return self.heap_size

    def root(self) -> int:
        """
        Returns the root of the heap

        Returns:
            int: Root value.
        """
        if not self.heap:
            return None
        return self.heap[0]

    def parent(self, i: int) -> int:
        """
        Returns the index of the parent of the given node index.

        Args:
            i (int): Index of node.

        Returns:
            int: Index of the parent of the node.
        """
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        """
        Returns the index of the left child of the given node index.

        Args:
            i (int): Index of node.

        Returns:
            int: Index of the left child of the node.
        """
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        """
        Returns the index of the right child of the given node index.

        Args:
            i (int): Index of node.

        Returns:
            int: Index of the right child of the node.
        """
        return 2 * i + 2

    def insert(self, value: int):
        """
        Inserts new value into the correct position.

        Args:
            value (int): New value.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        self.heap_size += 1

    def _heapify_up(self, i: int):
        """
        Switch node with parent until it is in the correct position.


        Args:
            i (int): Index of node.
        """
        if self.heap_type == "min":
            while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
                # Switch with parent
                self.heap[i], self.heap[
                    self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                i = self.parent(i)
        else:
            while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
                # Switch with parent
                self.heap[i], self.heap[
                    self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                i = self.parent(i)

    def _heapify_down(self, i: int):
        """
        Switch node with children until it is in the correct position.

        Args:
            i (int): Index of node.
        """
        left = self.left_child(i)
        right = self.right_child(i)

        if self.heap_type == "min":
            small = i
            # Determine which child to switch with
            if left < len(self.heap) and self.heap[left] < self.heap[small]:
                small = left
            if right < len(self.heap) and self.heap[right] < self.heap[small]:
                small = right

            if small != i:
                # Switch with child
                self.heap[i], self.heap[small] = self.heap[small], self.heap[i]
                self._heapify_down(small)
        else:
            big = i
            # Determine which child to switch with
            if left < len(self.heap) and self.heap[left] > self.heap[big]:
                big = left
            if right < len(self.heap) and self.heap[right] > self.heap[big]:
                big = right

            if big != i:
                # Switch with child
                self.heap[i], self.heap[big] = self.heap[big], self.heap[i]
                self._heapify_down(big)

    def extract(self) -> int:
        """
        Extract element, either max-extract or min-extract.

        Returns:
            int: Value extracted.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        self.heap_size -= 1
        return value

    def print(self):
        """
        Prints first 3 rows of the heap into a nicely formatted manner.
        """
        if not self.heap:
            return
        size = len(self.heap[:15])
        print(f"HEAP {self.heap_type}")
        output = ""
        last_row = -1
        total_width = 2 ** (int(log2(size)) + 3)
        for i, n in enumerate(self.heap[:15]):
            if i:
                row = int(floor(log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output += "\n"
            columns = 2 ** row
            col_width = int(floor((total_width * 1.0) / columns))
            output += str(n).center(col_width, " ")
            last_row = row
        print('-' * total_width)
        print(output)
        print('-' * total_width)


# Define two heaps for median maintanence
HEAP_MAX = Heap("max")
HEAP_MIN = Heap("min")


def heap_median(small_root: int, big_root: int, size1: int, size2: int) -> int:
    """
    Finds the meadian using the two heaps.

    Args:
        small_root (int): Min heap root.
        big_root (int): Max heap root.
        size1 (int): Size of heap of the Min heap root.
        size2 (int): Size of heap of the Max heap root.

    Returns:
        int: Median.
    """
    if small_root is None and big_root is None:
        return None
    if small_root is None:
        return big_root
    if big_root is None:
        return small_root
    
    if size1 > size2:
        return small_root
    if size1 < size2:
        return big_root
    return min(small_root, big_root)


def heap_add_and_maintain(new_value: int) -> int:
    """
    Adds a new number to the heap and returns the median.

    Args:
        new_value (int): New number to add.

    Returns:
        int: Current median.
    """
    global HEAP_MAX
    global HEAP_MIN

    # Determine which heap to add the new element
    max_root = HEAP_MAX.root()
    min_root = HEAP_MIN.root()
    max_size = HEAP_MAX.size()
    min_size = HEAP_MIN.size()
    median = heap_median(min_root, max_root, min_size, max_size)
    selected_heap = None

    if max_root is None and min_root is None:
        selected_heap = "min"
    elif max_root is None:
        selected_heap = "min"
    elif min_root is None:
        selected_heap = "max"
    else:
        if new_value <= median:
            selected_heap = "max"
        else:
            selected_heap = "min"

    # Add the element
    if selected_heap == "max":
        HEAP_MAX.insert(new_value)
        max_size += 1
    else:
        HEAP_MIN.insert(new_value)
        min_size += 1

    # Fix potential inbalance
    if abs(max_size - min_size) > 1:
        if max_size > min_size:
            extracted_node = HEAP_MAX.extract()
            HEAP_MIN.insert(extracted_node)
        else:
            extracted_node = HEAP_MIN.extract()
            HEAP_MAX.insert(extracted_node)

    # Return median value
    max_root = HEAP_MAX.root()
    min_root = HEAP_MIN.root()
    max_size = HEAP_MAX.size()
    min_size = HEAP_MIN.size()
    median = heap_median(min_root, max_root, min_size, max_size)
    return median
