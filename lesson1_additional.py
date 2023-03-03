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
    if price.isdigit():
        price = int(price)
        list.append({'name': name, 'price': price})
        print(list)
    else:
        input('price must be a number')


def show_shopping_list(shopping_list):
    print(shopping_list)


def sum_shopping_list(list):
    sum_price = []
    for ch in list:
        price = ch.get('price')
        sum_price.append(price)
    print(sum(sum_price))


def max_shopping_list(list):
    max_price = []
    for ch in list:
        price = ch.get('price')
        max_price.append(price)
    print(max(max_price))


def search(list):
    info = input('Enter name: ')
    for ch in list:
        name = ch.get('name')
        price = ch.get('price')
        if name == info:
            print('name:', name, 'price:', price)


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
