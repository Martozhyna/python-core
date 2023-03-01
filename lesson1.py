# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# def num(string):
#     print(' ,'.join(ch for ch in string if ch.isdigit()))
#
#
# st = 'as 23 fdfdg544'
#
# num(st)
# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################
#
# st = 'as 23 fdfdg544 34'
# print(', '.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))


# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# print([ch.upper() for ch in greeting])
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([i * i for i in range(51) if i % 2 != 0])


#
# function
#
# - створити функцію яка виводить ліст

# def list1(ls):
#     print(ls)
#
#
# list1([1, 2, 3])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def m(num1, num2, num3):
#     print(max(num1, num2, num3))
#
#
# m(-10, 0, 29)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_and_max_numbers(*args):
#     print(max(args))
#     return min(args)


# min_and_max_numbers(2, 7, -98, 0, 54, 3)


# - створити функцію яка повертає найбільше число з ліста

def max_in_list(some_list):
    return max(some_list)


# - створити функцію яка повертає найменьше число з ліста

def mim_in_list(some_list):
    return min(some_list)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_lists_number(some_list):
    sum_numbers = 0
    for i in some_list:
        sum_numbers += i
    return sum_numbers


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#
#

def average_numbers(some_list):
    avr = 0
    for i in some_list:
        avr += i

    print(avr / len(some_list))


average_numbers([1, 6, 5, 4])
#
# ################################################################################################
# 1)Дан list:
ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - знайти мін число
print(min(ls))
#   - видалити усі дублікати
print(set(ls))
#   - замінити кожне 4-те значення на 'X'
print([item if (i + 1) % 4 != 0 else 'X' for i, item in enumerate(ls)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


square(11)


# 3) вывести табличку множення за допомогою цикла while
def multi():
    i = 1
    while i < 10:
        j = 1
        while j < 10:
            res = i * j
            print(' ' if res//10 else '  ', end='')
            print(res, end='')
            j += 1
        print('')
        i += 1


multi()

# 4) переробити це завдання під меню

def menu():
    while True:
        print('1) знайти мін число')
        print('2) видалити усі дублікати')
        print("3) замінити кожне 4-те значення на 'X'")
        print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
        print('5) вывести табличку множення за допомогою цикла while')
        print('9) Вихід')

        ch = input('make your choose: ')

        if ch == '1':
            ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
            print(min(ls))
        elif ch == '2':
            ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
            print(set(ls))
        elif ch == '3':
            ls = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
            print([item if (i + 1) % 4 != 0 else 'X' for i, item in enumerate(ls)])
        elif ch == '4':
            square(10)
        elif ch == '5':
            multi()
        elif ch == '9':
            break


menu()
