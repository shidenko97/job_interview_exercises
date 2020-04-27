"""
https://leetcode.com/articles/reverse-integer/
"""

MAX_INT: int = 2 ** 31 - 1
MIN_INT: int = -2 ** 31
NUMBERS: tuple = (123, -123, 120, 3, 10, 11, -445, 234, 1001, 2000, 102030405)


def reverse_int(number: int) -> int:
    """
    Reverse integer
    :param number: The number to reverse
    :type number: int
    :return: The reversed number
    :rtype: int
    """

    is_negative: bool = False if number > 0 else True
    result: int = 0

    # Check MIN and MAX limits
    if MIN_INT > number or MAX_INT < number:
        return result

    number = abs(number)

    while number != 0:
        # Get last digit of the number and move the number on one digit to left
        pop = number % 10
        number //= 10

        # Move the number on one digit to right and plus popped digit
        result = result * 10 + pop

    return result * -1 if is_negative else result


if __name__ == "__main__":
    for num in NUMBERS:
        reversed_number = reverse_int(num)
        print(f"Reversed {num} is {reversed_number}")
