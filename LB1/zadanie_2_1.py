import re
import os

def is_invalid_name(name):
    # Проверяем, что имя начинается с маленькой буквы или содержит недопустимые символы
    if name[0].islower() or not name[0].isalpha():  # Имя начинается с маленькой буквы или с другого символа
        return True
    if not re.match("^[a-zA-Zа-яА-ЯёЁ]+$", name):  # Имя содержит недопустимые символы
        return True
    return False

def greet_from_file(filename):
    # Путь к папке LB1
    folder_path = "LB1"
    
    # Создаем папку LB1, если она не существует
    os.makedirs(folder_path, exist_ok=True)
    
    # Путь к файлам
    names_file_path = os.path.join(folder_path, "names.txt")
    error_file_path = os.path.join(folder_path, "error.txt")
    
    try:
        # Открываем файл names.txt в папке LB1
        with open(names_file_path, "r") as file:
            names = file.readlines()
        
        for name in names:
            name = name.strip()  # Убираем лишние пробелы и символы новой строки
            if is_invalid_name(name):
                # Если имя начинается с маленькой буквы или другого символа,
                # записываем ошибку в файл error.txt
                with open(error_file_path, "a") as error_file:
                    error_file.write(f"Error: Invalid name '{name}'\n")
            else:
                # Если имя начинается с большой буквы, выводим приветствие
                print(f"Hello, {name}!")
                
    except FileNotFoundError:
        print("File not found.")
        with open(error_file_path, "a") as error_file:
            error_file.write("Error: Names file not found.\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        with open(error_file_path, "a") as error_file:
            error_file.write(f"Error: {e}\n")

# Вызов функции с именем файла, содержащего список имен
greet_from_file("LB1/names.txt")
