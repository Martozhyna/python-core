# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


# def notebook():
#     todolist = ['clean', 'wash']
#
#     def add_todo(todo):
#         nonlocal todolist
#         todolist.append(todo)
#         return todo
#
#     def get_all():
#         return todolist
#
#     return [add_todo, get_all]
#
#
# add_todo, get_all = notebook()
#
# print(add_todo('shopping'))
#
# print(get_all())


# 2) протипізувати перше завдання


# def notebook() -> list:
#     todolist: list[str] = ['clean', 'wash']
#
#     def add_todo(todo: str) -> None:
#         nonlocal todolist
#         todolist.append(todo)
#
#     def get_all() -> list[str]:
#         return todolist
#
#     return [add_todo, get_all]
#
#
# add_todo, get_all = notebook()
#
# print(add_todo('shopping'))
#
# print(get_all())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    num = str(num)
    numeric: list[str] = []
    st: str = ' '
    for i, ch in enumerate(num):
        if ch != "0":
            numeric.append(ch + '0' * (len(num) - i - 1))
            st = ' + '.join(numeric)
    print(st)
    return st


expanded_form(1010)

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій
# def counter(func):
#     count = 0
#
#     def inner(*args, **kwargs):
#         func(*args, **kwargs)
#         nonlocal count
#         count += 1
#         print('count: ', count)
#         return count
#
#     return inner
#
#
# @counter
# def greeting(name):
#     print('hello', name)
#
#
# greeting('max')
# greeting('max')
# greeting('max')
# greeting('veronica')