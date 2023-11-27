# Задача №21. Напишите программу для печати всех уникальных значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
              {"VII": " S005 "}, {" V ":" S009 "}, {" VIII": " S007 "}]

list = []

for i in range(len(dictionary)):
    for j in dictionary[i]:
        if dictionary[i][j] not in list:
            list.append(dictionary[i][j])
print("Вот все уникальные значения которые есть в словаре; ",list)
