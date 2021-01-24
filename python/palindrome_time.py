from random import choice
from string import ascii_uppercase, digits
from time import time
from typing import Callable

import matplotlib.pyplot as plt


def random_string_generator(is_palindrome: bool, length: int) -> str:
    string = "".join(choice(ascii_uppercase + digits) for _ in range(length))

    if is_palindrome:
        return string

    middle = len(string) // 2
    half = string[:middle]

    return half + half[::-1]


def time_it(number: int) -> Callable:
    def outer_wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs) -> float:
            start_time = time()
            for _ in range(number):
                func(*args, **kwargs)
            finish_time = time()
            execution_time = finish_time - start_time
            print(
                f"Execution time of {func.__name__} ({number} times) "
                f"is {execution_time} sec."
            )
            return execution_time
        return inner_wrapper
    return outer_wrapper


@time_it(number=10000)
def is_palindrome_slow(string: str) -> bool:
    return string == string[::-1]


@time_it(number=10000)
def is_palindrome_fast(string: str) -> bool:
    length = len(string)
    middle = (length // 2)
    delta = int(length % 2 == 0)
    return string[:middle] == string[length:middle - delta:-1]


@time_it(number=10000)
def is_palindrome_very_fast(string: str) -> bool:
    data = memoryview(bytes(string, encoding="utf-8"))
    return data == data[::-1]


@time_it(number=10000)
def is_palindrome_too_fast(string: str) -> bool:
    data = memoryview(bytes(string, encoding="utf-8"))
    length = len(data)
    middle = (length // 2)
    delta = int(length % 2 == 0)
    return data[:middle] == data[length:middle - delta:-1]


if __name__ == "__main__":
    CHARACTER_COUNTS = (100, 1000, 10000, 100000, 1000000, )
    slow_time = []
    fast_time = []
    very_fast_time = []
    too_fast_time = []

    for length in CHARACTER_COUNTS:
        for is_palindrome in (True, False):
            sign = "" if is_palindrome else "not "
            print(f"Testing {sign}palindrome string of {length} characters")
            string = random_string_generator(
                length=length, is_palindrome=is_palindrome
            )
            slow_time.append(is_palindrome_slow(string))
            fast_time.append(is_palindrome_fast(string))
            very_fast_time.append(is_palindrome_very_fast(string))
            too_fast_time.append(is_palindrome_too_fast(string))

    plt.plot(CHARACTER_COUNTS, slow_time[::2], label="Slow palindrome")
    plt.plot(CHARACTER_COUNTS, fast_time[::2], label="Fast palindrome")
    plt.plot(
        CHARACTER_COUNTS, very_fast_time[::2], label="Very fast palindrome"
    )
    plt.plot(CHARACTER_COUNTS, too_fast_time[::2], label="Too fast palindrome")

    plt.plot(CHARACTER_COUNTS, slow_time[1::2], label="Slow not palindrome")
    plt.plot(CHARACTER_COUNTS, fast_time[1::2], label="Fast not palindrome")
    plt.plot(CHARACTER_COUNTS, very_fast_time[1::2],
             label="Very fast not palindrome")
    plt.plot(
        CHARACTER_COUNTS, too_fast_time[1::2], label="Too fast not palindrome"
    )

    plt.xlabel("Characters count")
    plt.ylabel("Execution time (sec.)")

    plt.title("Is palindrome functions execution time")

    plt.legend()

    plt.show()

"""
As a result we can see significant performance with memoryview usage for true 
palindromes (6.99 and 3.72 sec. VS 0.85 and 0.86 sec. respectively in 1M 
characters string), but worst performance in case of not palindrome string 
(7.03 and 3.95 sec. VS 22.81 and 11.82 sec. respectively in 1M characters 
string).
"""
