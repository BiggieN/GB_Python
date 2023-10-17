# Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

import os

os.system("cls")

# 0 1 1 2 3 5 8

n = int(input("Enter number  "))
a = 1
b = 0
i = 1
fibonacci = 0
count = 0

while i <= n + 1:
    if fibonacci == n:
        break
    fibonacci = a + b
    a = b
    b = fibonacci
    i += 1
else:
    i = -1
print(i)