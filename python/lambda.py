if __name__ == "__main__":
    # Lambda function assigned to variable
    a = lambda a: a ** a

    print(a(2))

    # Lambda function with instant execution
    print((lambda b: b + b)(3))

    # Assigning to variable lambda depends on sign
    sign = True
    func = sign and (lambda k: k * 2) or (lambda k: k * 3)

    print(func(2))

    sign = False
    func = sign and (lambda k: k * 2) or (lambda k: k * 3)

    print(func(2))

    # One more case
    sign = True
    func = (lambda k: k * 2) if sign else (lambda k: k * 3)

    print(func(2))

    sign = False
    func = (lambda k: k * 2) if sign else (lambda k: k * 3)

    print(func(2))
