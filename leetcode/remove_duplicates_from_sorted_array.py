"""
https://leetcode.com/articles/remove-duplicates-from-sorted-array
"""

LISTS: tuple = (
    [],
    [1, 1, 2],
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
)


def remove_dup(array: list) -> int:
    """
    Remove duplicates from sorted array
    :param array: The list of sorted numbers
    :type array: list
    :return: Count of unique elements in list
    :rtype: int
    """

    array_len: int = len(array)

    # If input array is empty - return zero
    if not array_len:
        return 0

    i: int = 0  # Counter of unique elements in list
    for j in range(1, array_len):
        # If not duplicate - relocate element to start and increment counter
        if array[j] != array[i]:
            i += 1
            array[i] = array[j]

    return i + 1


if __name__ == "__main__":
    for arr in LISTS:
        unique_len = remove_dup(arr)
        print(f"Result of {arr} is {unique_len} - {arr[:unique_len]}")
