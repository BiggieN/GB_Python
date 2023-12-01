# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
from typing import NoReturn

def show_all(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        print("".join(data))
        # for i in enumerate(data):
        #     print(i.split('\n'))

def remove(file_name: str):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    data = ""
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        s = f"{last_name}, {first_name}, {patronymic}, {phone_number}\n"
        data.remove(s)
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(data)

def modify(file_name: str):
    # print("Введите данные для поиска:\n")
    # last_name = input("Введите фамилию: ")
    # first_name = input("Введите имя: ")
    # patronymic = input("Введите отчество: ")
    # phone_number = input("Введите номер телефона: ")
    old_data = find_by_attribute(file_name, True)
    print("Введите новые данные:\n")

    last_name_ = input("Введите фамилию: ")
    first_name_ = input("Введите имя: ")
    patronymic_ = input("Введите отчество: ")
    phone_number_ = input("Введите номер телефона: ")

    data = ""
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f"{last_name_}, {first_name_}, {patronymic_}, {phone_number_}\n"
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(data)

def find_by_attribute(file_name:str, option:bool):

    c = input("Введите 1 для поиска по фамилиию 2 для поиска по имени: ")
    opt = 0
    if c == '1':
        opt = 0
    elif c == "2":
        opt = 1
    attr = input("Введите имя\фамилию для поиска: ")
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(", ")[opt] == attr,data))
        print(list(zip(range(1,len(data)+1),data)))
        if option:
            id = input("Введите id нужного пользователя для изменения данных: ")
        else:
            id = input("Введите id нужного пользователя:")
        return data[int(id)-1]

def add_new(file_name: str) -> None:
    """
    Функция принимает имя файла (file_name) в виде строки,
    запрашивает у пользователя данные в виде ФИО и номер телефона
    и сохранили полученные данные в файл.
    :param file_name: str имя файла
    :return: None
    """
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    with open(file_name, "a", encoding="utf-8") as fd:
        fd.write(f"{last_name}, {first_name}, {patronymic}, {phone_number}\n")

def copy(file_name: str, copy_file_name: str):
    #with open(file_name, "r", encoding="utf-8") as f:
    #    data = f.readlines()
    #    for i in enumerate(data, start=1):
    #        print(i)
    #    position = input("Введите номер записи, которую нужно скопировать: ")
    data = ""
    with open(file_name, "r", encoding="utf-8") as source, open(copy_file_name, "a", encoding="utf-8") as destination:
        data = source.readlines()
        for i in enumerate(data, start=1):
            print(i)
        position = int(input("Введите номер записи, которую нужно скопировать: "))
        destination.writelines(data[position-1])
    
def main():
    flag_exit = False
    file_name = "phonebook.txt"
    copy_file_name = "copy-phonebook.txt"
    while not flag_exit:
        print("1 - показать все записи")
        print("2 - добавить запись")
        print("3 - удалить запись")
        print("4 - изменить запись")
        print("5 - поиск записи по имени\фамилии")
        print("6 - скопировать запись во второй файл")
        answer = input("Введите операцию или x для выхода: ")
        if answer == "1":
            show_all(file_name)
        elif answer == "2":
            add_new(file_name)
        elif answer == "3":
            remove(file_name)
        elif answer == "4":
            modify(file_name)
        elif answer == "5":
            print(find_by_attribute(file_name, False))
        elif answer == "6":
            copy(file_name, copy_file_name)
        elif answer == "x":
            flag_exit = True
    
if __name__ == "__main__":
    main()