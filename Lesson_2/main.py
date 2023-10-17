# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input("Введите число "))

res = sum(map(int,str(n)))
print(res)