class A:

    def method1(self):
        print("Class A method1")

    def method2(self):
        print("Class A method2")

    def method5(self):
        print("Class A method5")


class B:

    def method2(self):
        print("Class B method2")

    def method5(self):
        print("Class B method5")


class C(B):

    def method3(self):
        print("Class C method3")


class D(C, A, B):
    """
    Inherits classes by search in depth algorithm,
    but in case of duplicate keep last occurrence
    """

    def method4(self):
        print("Class D method4")


if __name__ == "__main__":
    d = D()

    print(D.__mro__)

    d.method1()
    d.method2()
    d.method3()
    d.method4()
    d.method5()
