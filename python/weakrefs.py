import gc
import weakref


class Test:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


if __name__ == "__main__":
    # Create new class' instance
    test = Test(10)

    print(test)

    # Create dictionary of weak references
    d = weakref.WeakValueDictionary()

    # Add current instance to weak dictionary
    d["primary"] = test

    print(d["primary"])

    # Delete class' instance
    del test

    # Run Garbage collector
    gc.collect()

    # Handle error about deleted instance
    print(d["primary"])
