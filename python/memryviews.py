import time


if __name__ == "__main__":

    # Slicing a large string (slow)
    for n in (100000, 200000, 300000, 400000):
        data = "x" * n
        start = time.time()
        b = data

        while b:
            b = b[1:]

        print(f"String: {n} - {time.time() - start}")

    # Slicing a large memoryview object (faster)
    for n in (100000, 200000, 300000, 400000):
        data = "x" * n
        start = time.time()
        b = memoryview(bytes(data, encoding="utf8"))

        while b:
            b = b[1:]

        print(f"String: {n} - {time.time() - start}")
