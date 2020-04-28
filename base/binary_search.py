def binary_search_iter(array: list, el: int) -> int:
    """
    Iterative binary search
    :param array: Array to search
    :type array: list
    :param el: Element to search
    :type el: int
    :return: Found element or -1 if not found
    :rtype: int
    """

    low: int = 0
    high: int = len(array) - 1

    while low <= high:
        mid: int = (low + high) // 2

        if array[mid] > el:
            high = mid - 1
        elif array[mid] < el:
            low = mid + 1
        else:
            return mid

    return -1


def binary_search_recv(
        array: list,
        el: int,
        low: int = 0,
        high: int = 0
) -> int:
    """
    Recursive binary search
    :param array: Array to search
    :type array: list
    :param el: Element to search
    :type el: int
    :param low: Lowest index in array
    :type low: int
    :param high: Highest index in index
    :type high: int
    :return: Found element or -1 if not found
    :rtype: int
    """

    high = high or len(array) - 1

    if high < low:
        return -1

    mid: int = (low + high) // 2

    if array[mid] > el:
        return binary_search_recv(array, el, low, mid - 1)
    elif array[mid] < el:
        return binary_search_recv(array, el, mid + 1, high)
    else:
        return mid


if __name__ == "__main__":
    for i in (-1000, -2, -1, 0, 1, 498, 499, 500, 501, 998, 999, 1000, 1001):
        print(
            i,
            binary_search_iter(list(range(0, 1000)), i),
            binary_search_recv(list(range(0, 1000)), i)
        )
