def bubble_sort(array: list) -> list:
    """
    Bubble sort
    Time complexity O(n^2)
    :param array: Array to sort
    :type array: list
    :return: Sorted array
    :rtype: list
    """

    # Sign that shows if sort was did in current iteration
    is_sorted: bool = False
    # Index of last element in list
    last: int = len(array) - 1

    # Outer and inner cycles for sorting
    for _ in range(last):
        for index in range(last):

            # If left element greater then right element - swap it
            # and set sorted sign
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                is_sorted = True

        # If list not sorted after iteration - stop iterations
        if not is_sorted:
            break

        is_sorted = False

    return array


if __name__ == "__main__":
    tuples = (
        [1, 2, 3, 4, 8, 7, 6, 5],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [4, 3, 2, 1, 8, 7, 6, 5],
        [2, 3, 4, 1, 6, 8, 7, 5],
        [4, 3, 6, 2, 1, 7, 8, 5]
    )
    for arr in tuples:
        print(f"Before sort: {arr}")
        print(f"After sort: {bubble_sort(arr)}")
