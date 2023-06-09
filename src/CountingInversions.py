def CountInversions(arr: list[int], length: int) -> tuple[list[int], int]:
    if length == 1 or length == 0:
        return arr, 0
    else:
        half_length = int(length/2)
        # Recursively divide the array into two halves and count inversions
        arr1, x = CountInversions(arr[:half_length], half_length)
        arr2, y = CountInversions(
            arr[half_length:],
            half_length + 1 if length & 1 else half_length
        )
        # Merge the divided arrays and count split inversions
        arr3, z = CountSplitInversion(arr1, arr2)
    return arr3, x+y+z


def CountSplitInversion(arr1: list[int], arr2: list[int]) -> tuple[list[int], int]:
    result = []
    inversions = 0
    size_left = len(arr1)
    size_right = len(arr2)
    left_index = 0
    right_index = 0

    # Merge the two arrays by doing a linear scan concurrently
    while left_index < size_left and right_index < size_right:
        if arr1[left_index] <= arr2[right_index]:
            result.append(arr1[left_index])
            left_index += 1
        else:  # Inversion case
            result.append(arr2[right_index])
            inversions += size_left - left_index
            right_index += 1

    # Append remaining elements from the left or right array
    if left_index < size_left:
        result.extend(arr1[left_index:])
    else:  # Count any remaining split inversions
        result.extend(arr2[right_index:])
        inversions += size_left - left_index
    return result, inversions
