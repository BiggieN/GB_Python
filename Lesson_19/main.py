# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число

list_num = [1, 2, 3, 4, 5]
k = 3

for i in range(k):
    list_num.insert(0, list_num.pop())

print(list_num)