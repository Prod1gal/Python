"""

Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

"""

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(max(number_1, number_2, number_3))
print(min(number_1, number_2, number_3))

if (number_1 <= number_2 and number_1 >= number_3) or (number_1 >=number_2 and number_1 <= number_3):
    print(number_1)
elif (number_2 <= number_3 and number_2 >=number_1) or (number_2 >= number_3 and number_2 <= number_1):
    print(number_2)
else:
    print(number_3)