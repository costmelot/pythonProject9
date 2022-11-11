# numbers = [1, 2, 3, 5, 1, 5, 3, 10]
# unique_numbers = list(set(numbers))
# print(unique_numbers)
from collections import OrderedDict

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print("Оригинальный список : " + str(my_list))

result = set()
res = set()

for num in my_list:
    if num not in result:
        result.add(num)
    else:
        res.add(num)
unique = list(result - res)
print("Список уникальных значений: " + str(unique))

dup = {x for x in my_list if my_list.count(x) > 1}
print("Список повторяющихся значений: " + str(list(dup)))

li = list(OrderedDict.fromkeys(my_list))

print("Список после удаления дубликатов: " + str(li))
