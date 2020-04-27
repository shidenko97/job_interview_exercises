# Tasks

## First
Есть задача – удалить из текста некоторые «мусорные» слова. 
Решает ли приведенный ниже код эту задачу?
Если нет, перечислите его недостатки, необходимые доработки и тд.

```python
# список мусорных слов
unmeaningful = ['the', 'this', 'that', 'our', 'a', 'and']
text = """
    This property is also rated for the best value in London! 
    Guests are getting more for their money when compared to other 
    properties in this city.
"""

for w in unmeaningful:
    text = text.replace(w, '')

print(text)
```

## Second
Что будет выведено на экран в результате выполнения программы?

```python
nums = range(10)
nums3 = [2*i for i in nums if i < 7]

print(nums3)
```

## Third
Есть ли какая-то разница между объектами words? 
Чем отличается обычный for loop от comprehension?

```python
doc = (
    ("One", "two", "third"),
    ("Fourth", "fifth", "sixth"),
    ("Seventh", "eighth", "ninth"),
    ("eighth", "third", "Fourth"),
)

words1 = (word for sentence in doc for word in sentence)
words2 = [word for sentence in doc for word in sentence]
words3 = {word for sentence in doc for word in sentence}
```

## Fourth
Что выведется на экран в результате выполнения кода?

```python
def fruits(index):
    all_fruits = ['apple', 'banana', 'pineapple']

    for _ in all_fruits:
        yield all_fruits[index]


my_fruit = fruits(0)

print(my_fruit)

while True:
    print(next(my_fruit))
```

## Fifth
Рассмотрите два подхода ниже для инициализации списка и списков. 
В чём разница между этими подходами и почему следует использовать 
только один из них?

```python
# Инициализация списка -- метод 1
x = [[1,2,3,4]] * 3 
# [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

# Инициализация списка -- метод 2
y = [[1,2,3,4] for _ in range(3)]
# [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
```