"""
Overloads standard get, set, delete operations for class' attributes.

If any of three methods are defined - it's a descriptor.
If __get__ and __set__ are defined - it's a data descriptor.
If only __get__ is defined - it's a non-data descriptor.
"""


class DecoratorDescriptor:
    """Class with decorator descriptor."""

    def __init__(self, attribute):
        self._private_attribute = attribute

    @property
    def private_attribute(self):
        return self._private_attribute * 10

    @private_attribute.setter
    def private_attribute(self, value):
        self._private_attribute = value

    @private_attribute.deleter
    def private_attribute(self):
        self._private_attribute = 0

    def __repr__(self):
        return f"Test(attribute={self._private_attribute})"


class PropertyDescriptor:
    """Class with property descriptor."""

    def __init__(self, attribute):
        self._private_attribute = attribute

    def fget(self):
        return self._private_attribute * 10

    def fset(self, value):
        self._private_attribute = value

    def fdel(self):
        self._private_attribute = 0

    private_attribute = property(fget=fget, fset=fset, fdel=fdel)

    def __repr__(self):
        return f"Test(attribute={self._private_attribute})"


class Descriptor:
    """Class with simple descriptor."""

    def __init__(self, attribute):
        self._private_attribute = attribute

    def __get__(self, instance, owner):
        return self._private_attribute * 10

    def __set__(self, instance, value):
        self._private_attribute = value

    def __delete__(self, instance):
        self._private_attribute = 0

    def __repr__(self):
        return f"Test(attribute={self._private_attribute})"


if __name__ == "__main__":
    dd = DecoratorDescriptor(1)

    print(dd)

    print(f"Getter: {dd.private_attribute}")

    dd.private_attribute = 2

    print(dd)

    print(f"Getter: {dd.private_attribute}")

    del dd.private_attribute

    print(dd)

    print(f"Getter: {dd.private_attribute}")

    pd = PropertyDescriptor(1)

    print(pd)

    print(f"Getter: {pd.private_attribute}")

    pd.private_attribute = 2

    print(pd)

    print(f"Getter: {pd.private_attribute}")

    del pd.private_attribute

    print(pd)

    print(f"Getter: {pd.private_attribute}")

    d = Descriptor(1)

    print(d)

    print(f"Getter: {d._private_attribute}")

    d._private_attribute = 2

    print(d)

    print(f"Getter: {d._private_attribute}")

    del d._private_attribute

    print(d)

    print(f"Getter: {d._private_attribute}")
