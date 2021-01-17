import time


def time_it(func):
    """
    Simple decorator to calculate execution time without additional arguments
    """
    def wrapper():
        start_time = time.time()
        result = func()
        print(f"Execution time: {time.time() - start_time}")

        return result

    return wrapper


def time_it_with_text(text="Execution time:"):
    """
    Simple decorator to calculate execution time with additional arguments
    """
    def outer_wrapper(func):
        def wrapper():
            start_time = time.time()
            result = func()
            print(f"{text} {time.time() - start_time}")

            return result
        return wrapper

    return outer_wrapper


class TimeIt:
    """Class decorator to calculate execution time with additional arguments"""

    def __init__(self, text="Hello, it's me: "):
        self.text = text

    def __call__(self, func):
        def wrapper():
            start_time = time.time()
            result = func()
            print(f"{self.text} {time.time() - start_time}")

            return result

        return wrapper


@time_it
def loops():

    arr = []

    for i in range(10):
        time.sleep(0.1)
        arr.insert(0, 1)

    return arr


@time_it_with_text(text="Hi, man: ")
def loops_with_text():

    arr = []

    for i in range(10):
        time.sleep(0.1)
        arr.insert(0, 1)

    return arr


@TimeIt(text="bla:")
def loops_by_class():

    arr = []

    for i in range(10):
        time.sleep(0.1)
        arr.insert(0, 1)

    return arr


if __name__ == "__main__":
    print(loops())
    print(loops_with_text())
    print(loops_by_class())
