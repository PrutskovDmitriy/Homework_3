numb_free = str(input('Чило от 1 до 10 на английском: '))
dict1 = {'one': 'один',
         'two': 'два',
         'three': 'три',
         'four': 'четыре',
         'five': 'пять',
         'six': 'шесть',
         'seven': 'семь',
         'eight': 'восемь',
         'nine': 'девять',
         'ten': 'десять'}
def numbs_translate(eng_word):
        if eng_word[0] == eng_word[0].upper():
                eng_word = eng_word.lower()
                return dict1[eng_word].capitalize()
        else:
                return dict1.get(eng_word)
print(numbs_translate(numb_free))
# dict2 = {'One': 'Oдин',
#         'Two': 'Два',
#         'Three': 'Три',
#         'Four': 'Четыре',
#         'Five': 'Пять',
#         'Six': 'Шесть',
#         'Seven': 'Семь',
#         'Eight': 'Восемь',
#         'Nine': 'Девять',
#         'Ten': 'Десять'}
# dict1.update(dict2)
# if numb_free in dict1:
#         print('Ваше число: ', dict1[numb_free])
# else:
#         print('Нет такого числа или не существует')

