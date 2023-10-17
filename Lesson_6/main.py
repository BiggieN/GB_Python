# Задача 6. Проверить на счастливое число

n = int(input("Введите число "))

lucky = []
while n > 0:
   lucky.append(n % 10)
   n = n // 10
l1 = int(lucky[0]) + int(lucky[1]) + int(lucky[2])
l2 = int(lucky[3]) + int(lucky[4]) + int(lucky[5])
if l1 == l2:
    print("yes")
else:
    print("no")