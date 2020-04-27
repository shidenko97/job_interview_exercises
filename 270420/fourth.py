# Будет выведено объект генератора, а потом 3 раза 'apple', после чего
# сработает исключение StopIteration, в связи с тем что yield возвращает
# объект генератора и по нему необходимо итерироваться для получения значения.


def fruits(index):
    all_fruits = ['apple', 'banana', 'pineapple']

    for _ in all_fruits:
        yield all_fruits[index]


my_fruit = fruits(0)

print(my_fruit)

while True:
    print(next(my_fruit))
