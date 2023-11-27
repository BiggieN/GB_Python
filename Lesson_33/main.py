# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

def grades_correction (array, i, max_num):
    if i == -1:
        return
    if array[i] == max_num:
        array[i] = min(array)
    return grades_correction (array, i - 1, max_num)

array = [1, 3, 3, 3, 4]
grades_correction(array, len(array)-1, max(array))
print(*array)