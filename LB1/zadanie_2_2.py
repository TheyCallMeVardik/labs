import os

# Папка для хранения ошибок
error_file_path = os.path.join("LB1", "error1.txt")

# Функция для записи ошибок в файл
def log_error(error_message):
    if not os.path.exists("LB1"):
        os.makedirs("LB1")
    with open(error_file_path, "a") as file:
        file.write(error_message + "\n")

try:
    while True:
        # Запрашиваем имя у пользователя
        name = input("Введите ваше имя: ")

        # Проверяем, что имя начинается с заглавной буквы
        if name[0].isupper():
            print(f"Привет, {name}!")
            break
        else:
            log_error(f"Error: Name '{name}' does not start with an uppercase letter.")
            print("Имя должно начинаться с заглавной буквы. Попробуйте снова.")
        
except KeyboardInterrupt:
    # Обработка остановки процесса через Ctrl+C
    print("\nGoodbye!")
