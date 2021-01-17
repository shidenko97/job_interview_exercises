def fibonacci(count):
    """Predefined length Fibonacci sequence generator function"""
    a = b = 1
    for _ in range(count):
        yield a
        a, b = b, a + b


class Fibonacci:
    """Infinitive length Fibonacci sequence generator class"""

    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a + self.b


if __name__ == "__main__":
    for number in fibonacci(10):
        print(number)

    one_element_fibonacci_sequence = fibonacci(1)
    print(next(one_element_fibonacci_sequence))

    try:
        print(next(one_element_fibonacci_sequence))
    except StopIteration as err:
        print(err)

    for number in Fibonacci():

        if number > 100:
            break

        print(number)

    a = iter(Fibonacci())
    print(next(a))
    print(next(a))
    print(next(a))
