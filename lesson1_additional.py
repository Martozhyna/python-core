# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

shopping_list = [
    {'name': 'water', 'price': 10},
    {'name': 'apples', 'price': 15},
    {'name': 'potato', 'price': 22}
]


def add_shopping(list):
    name = input('Enter name: ')
    price = input('Enter price: ')
    price = int(price)
    list.append({'name': name, 'price': price})
    print(list)


def show_shopping_list(shopping_list):
    print(shopping_list)


def sum_shopping_list(list):
    a = []
    for ch in list:
        q = ch.get('price')
        a.append(q)
    print(sum(a))


def max_shopping_list(list):
    a = []
    for ch in list:
        q = ch.get('price')
        a.append(q)
    print(max(a))


def search(list):
    info = input('Enter name: ')
    for ch in list:
        x = ch.get('name')
        y = ch.get('price')
        if x == info:
            print('name:', x, 'price:', y)


def menu():
    while True:
        print('1) Создать запись')
        print('2) Список все записей')
        print('3) Общая сумма всех покупок')
        print('4) Самая дорогая покупка')
        print('5) Поиск по названию покупки')
        print('9) Выход')

        choice = input('make your choose: ')

        if choice == '1':
            add_shopping(shopping_list)
        elif choice == '2':
            show_shopping_list(shopping_list)
        elif choice == '3':
            sum_shopping_list(shopping_list)
        elif choice == '4':
            max_shopping_list(shopping_list)
        elif choice == '5':
            search(shopping_list)
        elif choice == '9':
            break


menu()
