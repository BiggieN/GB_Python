# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
from typing import NoReturn

def show_all():
    pass

def remove(file_name: str):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    data = ""
    with open(file_name, "r") as f:
        data = f.read()
        s = f"{last_name}, {first_name}, {patronymic}, {phone_number}\n"
        i = data.find()
        data = data[:i] + data[i+len(s)]
    with open(file_name, "w") as f:
        f.write(data)

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

def main():
    flag_exit = False
    file_name = "phonebook.txt"
    while not flag_exit:
        print("1 - показать все записи")
        print("2 - добавить запись")
        print("3 - удалить запись")
        answer = input("Введите операцию или x для выхода: ")
        if answer == "1":
            show_all()
        elif answer == "2":
            add_new(file_name)
        elif answer == "3":
            remove(file_name)
        elif answer == "x":
            flag_exit = True
    
if __name__ == "__main__":
    main()