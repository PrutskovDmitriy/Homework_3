import random
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# def get_jokes(num):
#     list1 = []
#     for i in range(num):
#         new_nouns = random.choices(nouns)
#         new_adverbs = random.choices(adverbs)
#         new_adjectives = random.choices(adjectives)
#         list1.append(f'{new_nouns} {new_adverbs} {new_adjectives}')
#     return list1
#
# print(get_jokes(1))
# print(get_jokes(5))

nouns = random.choices(["автомобиль", "лес", "огонь", "город", "дом"])
adverbs = random.choices(["сегодня", "вчера", "завтра", "позавчера", "ночью"])
adjectives = random.choices(["веселый", "яркий", "зеленый", "утопичный", "мягкий"])
for nouns, adverbs, adjectives in zip(nouns, adverbs, adjectives):
    print(nouns, adverbs, adjectives)
