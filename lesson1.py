# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################


# st = 'as 23 fdfdg544'
# num = ''
# a = ' ,'
# res = ''
#
# for ch in st:
#     if ch.isdigit():
#         num += ch
#         res = a.join(num)
#
#
# print(res)


# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
#################################################################################

#
#
# print(num)

# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
#
# greeting = 'Hello, world'
# l = []
#
# for ch in greeting:
#     l += ch.upper()
#
# print(l)
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l=[]
#
# for i in range(50):
#      l.append(i**2)
#
# print(l)

# function
#
# - створити функцію яка виводить ліст

# def li(ls):
#     print(ls)
#
#


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         print(num1)
#         return num1
#     elif num2 > num1 and num2 > num3:
#         print(num2)
#         return num2
#     elif num3 > num1 and num3 > num2:
#         print(num3)
#         return num3
#     else:
#         print(num1)
#
#
# max_num(7, 7, 7)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_and_max_number(*args):
#     max_number = max(args)
#     print(max_number)
#     min_number = min(args)
#     return min_number
#
#
# min_and_max_number(2, 3, 64, 234)

# - створити функцію яка повертає найбільше число з ліста

#
# def max_number_of_list(lst):
#      return max(lst)


# - створити функцію яка повертає найменьше число з ліста

# def min_number_of_list(lst):
#     return min(lst)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_of_number(lst):
#     result = 0
#     for i in lst:
#         result += i
#     print(result)
#     return result
#
# sum_of_number([1,2,3])

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def awe(lst):
#     result = 0
#     for i in lst:
#         result += i
#     return result/len(lst)

# 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#   - знайти мін число

# print(min(list))

#   - видалити усі дублікати

# numbers = []
# [numbers.append(num) for num in list if num not in numbers]
# print(numbers)

#   - замінити кожне 4-те значення на 'X'

# l = []
# for i,p in enumerate(list):
#     if not (i+1) % 4:
#         l.append('X')
#     else:
#         l.append(p)
# print(l)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції



# 3) вывести табличку множення за допомогою цикла while


# 4) переробити це завдання під меню



