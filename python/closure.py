def multiply(a):

    def internal_func(b):
        return a * b

    return internal_func


if __name__ == "__main__":
    multiply_to_5 = multiply(5)

    print(multiply_to_5(2), multiply_to_5(5), multiply_to_5(10))

    multiply_to_7 = multiply(7)

    print(multiply_to_7(2), multiply_to_7(5), multiply_to_7(10))
