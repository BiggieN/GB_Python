# Дан список чисел. Определите, сколько в нем встречается различных чисел.

from random import randint
list = []
for i in range(7):
    list.append(randint(-10, 10))
print(list)
print(len(set(list)))
print(set(list))