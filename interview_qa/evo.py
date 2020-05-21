from operator import mul


FOR_FROM = 1
FOR_TO = 10
MULTIPLIER = 2


# Problem
def mul_(start, finish, arr=None):
    arr = arr if arr is not None else []

    for i in range(start, finish):
        arr.append(lambda b: mul(i, b))

    return arr


# Solving
def closure(i_):
    def closure_(b_):
        return i_ * b_

    return closure_


def mul2_(start, finish, arr=None):
    arr = arr if arr is not None else []

    for i in range(start, finish):
        arr.append(closure(i))

    return arr


if __name__ == "__main__":
    print("Problem:")
    print([func(MULTIPLIER) for func in mul_(FOR_FROM, FOR_TO)], end="\n\n")
    print("Solving:")
    print([func(MULTIPLIER) for func in mul2_(FOR_FROM, FOR_TO)])
