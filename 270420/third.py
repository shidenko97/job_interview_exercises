# Первое отличие это тип данных - words1 это объект генератора, words2 это
# список, а words3 это множество. Второе отличие - в множестве могут быть
# только уникальные элементы и оно неупорядочено. Третее отличие - по объекту
# генератора нужно итерироваться, для получения результатов или же - привести
# в другой тип данных, но после окончания итерирования оно станет пустым, что
# делает его одноразовым для прохождения.

doc = (
    ("One", "two", "third"),
    ("Fourth", "fifth", "sixth"),
    ("Seventh", "eighth", "ninth"),
    ("eighth", "third", "Fourth"),
)

words1 = (word for sentence in doc for word in sentence)
words2 = [word for sentence in doc for word in sentence]
words3 = {word for sentence in doc for word in sentence}

print(words1, type(words1), list(words1))
print(words2, type(words2))
print(words3, type(words3))
