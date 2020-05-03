"""
https://leetcode.com/articles/remove-element/
"""

LISTS: tuple = (
    ([], None),
    ([3, 2, 2, 3], 3),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2),
    ([0, 1, 5, 6, 9, 3, 20, 58], 5)
)


def remove_element(nums: list, val: int):
    """
    Remove specific num from list and return result list's length
    :param nums: List of numbers
    :type nums: list
    :param val: Number to remove
    :type val: int
    :return: Length of result list
    """

    # Declare list offset and length of new list
    offset = length = 0

    for i in range(len(nums)):
        # Set index with offset
        real_index: int = i - offset

        # If element is needed - remove it and increment the offset
        # else - increment length of new list
        if nums[real_index] == val:
            del nums[real_index]
            offset += 1
        else:
            length += 1

    return length


if __name__ == "__main__":
    for arr, num in LISTS:
        print(
            f"remove_element({arr}, {num}) -> "
            f"{remove_element(arr, num)} -> "
            f"{arr}"
        )
