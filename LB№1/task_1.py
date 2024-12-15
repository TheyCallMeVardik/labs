import random
import sys
import math

if len(sys.argv) > 1 and sys.argv[1] == 'part1':
    A = random.randint(-10, 10)
    print(A)

elif len(sys.argv) > 1 and sys.argv[1] == 'part2':
    try:
        A = int(input("Введите число A: "))
        B = random.randint(-10, 10)
        while B == 0:
            B = random.randint(-10, 10)
            print(f"B = {B}")
        result = A / B
        print(f"Отношение A/B = {result:.2f}")
    except ValueError:
        print("Ошибка: введено некорректное число.")

elif len(sys.argv) > 1 and sys.argv[1] == 'part3':
    try:
        A = int(input("Введите число: "))
        if A < 0:
            raise ValueError("Квадратный корень из отрицательного числа не определён.")
        sqrt_result = math.sqrt(A)
        with open("output.txt", "w") as file:
            file.write(f"Square root of {A} = {sqrt_result:.2f}\n")
        print("Результат записан в файл output.txt.")
    except ValueError as e:
        print(f"Ошибка: {e}")

else:
    print("Пожалуйста, укажите часть программы: part1, part2 или part3.")
