# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

my_list = [5, 3, 4, 5, 6, (25, 10), 'abcd', (17, 20), 'abcd', (25, 10), 'w', 'z']

my_set = set()

for item in my_list:
    if my_list.count(item) > 1:
        my_set.add(item)
print(my_list)
print(list(my_set))
