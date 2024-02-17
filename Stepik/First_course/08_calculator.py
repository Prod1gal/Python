"""

Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число, второе число и операцию, после чего применяет операцию к введённым числам
("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.

"""

number_1 = float(input())
number_2 = float(input())
operation = input()

if operation == "+":
    result = number_1 + number_2
    print(result)
elif operation == "-":
    result1 = number_1 - number_2
    print(result1)
elif operation == "*":
    result2 = number_1 * number_2
    print(result2)
elif operation == "/":
    if number_2 == 0:
        print("Деление на 0!")
    else:
        result3 = number_1 / number_2
        print(result3)
elif operation == "mod":
    if number_2 == 0:
        print("Деление на 0!")
    else:
        result4 = number_1 % number_2
        print(result4)
elif operation == "pow":
    result5 = number_1 ** number_2
    print(result5)
elif operation == "div":
    if number_2 == 0:
        print("Деление на 0!")
    else:
        result6 = number_1 // number_2
        print(result6)
