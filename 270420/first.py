# Не решает, так как он удалит все вхождения подстрок в тексте, в том числе и
# внутри других слов. Предлагаю разделять слова по пробему и искать их
# вхождение в список «мусорных».

unmeaningful = ['the', 'this', 'that', 'our', 'a', 'and']
text = """
    This property is also rated for the best value in London! 
    Guests are getting more for their money when compared to other 
    properties in this city.
"""

print(" ".join([word for word in text.split(" ") if word not in unmeaningful]))
