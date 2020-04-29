def linear_search(array: list, el: int) -> int:
    """
    Iterative linear search
    Time complexity O(n)
    :param array: Array to search
    :type array: list
    :param el: Element to search
    :type el: int
    :return: Found index of element or -1 if not found
    :rtype: int
    """

    # Iterate by elements and it's indexes
    for index, element in enumerate(array):

        # If found an element - returns index
        if element == el:
            return index

    return -1


if __name__ == "__main__":
    for i in (999, 1000, 1001, 4499, 4500, 4501, 9998, 9999, 10000):
        print(
            i,
            linear_search(list(range(1000, 10000)), i)
        )
