class ClassWithSlots:
    """Class with slots. It provides better performance then usual class."""

    __slots__ = "name", "description", "age"

    def __init__(self, name, description, age):
        self.name = name
        self.description = description
        self.age = age


class ClassWithoutSlots:
    """Usual class."""

    def __init__(self, name, description, age):
        self.name = name
        self.description = description
        self.age = age


if __name__ == "__main__":
    class_with_slots = ClassWithSlots("Bob", "Robot", 102)
    print(
        class_with_slots.name,
        class_with_slots.description,
        class_with_slots.age
    )

    try:
        # With slots in class all attributes are predefined and
        # you cannot add any more in runtime
        class_with_slots.job = "Engineer"
    except AttributeError as err:
        print(err)

    class_without_slots = ClassWithoutSlots("Jack", "It's Jack", 11)

    # Any errors in usual class
    class_without_slots.job = "Engineer"

    print(
        class_without_slots.name,
        class_without_slots.description,
        class_without_slots.age
    )
    class_without_slots.job = "Kid"
