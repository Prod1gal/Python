"""

Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и
выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

"""

# первый вариант
def sum_digits(ticket_number):
    return sum(map(int, ticket_number))

ticket_number = input()
while len(ticket_number) > 6 or len(ticket_number) < 6:
    print("Введите 6 цифр")
    ticket_number = input()
middle = len(ticket_number) // 2  # середина
if middle == 0 or sum_digits(ticket_number[:middle]) == sum_digits(ticket_number[-middle:]):
    print('Счастливый')
else:
    print('Обычный')



# второй вариант
ticket_number = input("Введите 6 цифр: ")
while len(ticket_number) > 6 or len(ticket_number) < 6:
    print("Вы ввели неверное количество")
    ticket_number = input("Введите 6 цифр: ")

a = int(ticket_number) // 1000
a1 = a % 10
a2 = (a // 10) % 10
a3 = (a // 100) % 10

b = int(ticket_number) % 1000
b1 = b % 10
b2 = (b // 10) % 10
b3 = (b // 100) % 10

if (a3 + a2 + a1) == (b3 + b2 + b1):
    print("Счастливый")
else:
    print("Обычный")