# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант

from operator import itemgetter

my_diction = {'рюкзак': 3, 'котелок': 1, 'палатка': 8, 'байдарка': 15, 'шатер': 12, 'мангал': 3, 'спорт инвертарь': 3}
max_capacity_backpack = 25
weight = 0
capacity_backpack = 0
print("рюкзак: ", my_diction)
print("список вещей по максимально возможной грузоподьемности рюкзака в ", max_capacity_backpack, "кг")
for things, value in dict(sorted(my_diction.items(), key=itemgetter(1))).items():
    weight += my_diction[things]

    if weight <= max_capacity_backpack:
        print(things, ' = ', value)
        capacity_backpack += my_diction[things]

print("общий вес рюкзака c вещами: ", capacity_backpack)
