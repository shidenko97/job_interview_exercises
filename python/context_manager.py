from contextlib import contextmanager


class ContextManager:
    """Context managed implemented as class"""

    def __enter__(self):
        """Do some actions to open some connection or file etc and return it"""

        return []

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Do some actions as finish of process (regular or exception happened).
        If returns True - exception will not raised, otherwise - will raised.
        """

        return True


@contextmanager
def context_manager():
    """Context managed implemented as function"""

    yield []


if __name__ == "__main__":
    with ContextManager() as my_file:
        print(my_file)

    with context_manager() as my_file:
        print(my_file)
