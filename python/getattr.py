class TestGettingAttributes:

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        """Fire if attribute doesn't exists in class"""

        print("Call __getattr__")

    def __getattribute__(self, item):
        """
        Fire when trying to get any attribute of class (even non-existing)
        """

        print("Call __getattribute__")
        return super().__getattribute__(item)


if __name__ == "__main__":
    test = TestGettingAttributes("Hi")
    print(test.name)
    print(test.last_name)
