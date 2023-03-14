# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва
# записувати не потрібно)
import json

try:
    with open('emails.txt', 'r') as file:
        gmail = open('gmail_emails.txt', 'w')
        for line in file:
            email = line.split()
            if email[1].endswith('@gmail.com'):
                gmail.write(f'{email[1]}\n')
        gmail.close()
except Exception as err:
    print(err)


# shopping_list = [
#     {'id': 1, 'name': 'water', 'price': 10},
#     {'id': 2, 'name': 'apples', 'price': 15},
#     {'id': 3, 'name': 'potato', 'price': 22}
# ]


# try:
#     with open('shopping_list.json', 'w') as file:
#         json.dump(shopping_list, file)
#
# except Exception as err:
#     print(err)

# def show_all():
#     try:
#         with open('shopping_list.json') as a:
#             shop = json.load(a)
#             for sh in shop:
#                 print(sh)
#
#     except Exception as e:
#         print(e)

# show_all()

# def add(l):
#     name = input('Enter name: ')
#     price = input('Enter price: ')
#     id = 1
#
#     if price.isdigit():
#
#         price = int(price)
#         l.append({'id': id, 'name': name, 'price': price})
#         id = id + 1
#
#
#         try:
#             with open('shopping_list.json', 'w') as f:
#                 json.dump(l, f)
#
#
#         except Exception as e:
#             print(e)
#
#         print(l)
#     else:
#         input('price must be a number')
#
#
# add(shopping_list)
# add(shopping_list)

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналу:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)


class ShoppingBook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.shopping_list = []
        self.id_name = self.__gen_id()

    @staticmethod
    def __gen_id():
        id_name = 1
        while True:
            yield id_name
            id_name += 1

    def read(self):
        try:
            with open(self.file_name) as f:
                self.shopping_list = json.load(f)
        except Exception as er:
            self.write()

    def write(self):
        try:
            with open(self.file_name, 'w') as f:
                json.dump(self.shopping_list, f)
        except Exception as er:
            print(er)

    def show(self):
        try:
            with open(self.file_name) as a:
                shop = json.load(a)
                for sh in shop:
                    print(sh)

        except Exception as e:
            print(e)

    def add(self):
        name = input('Enter name: ')
        price = input('Enter price: ')
        if price.isdigit():
            price = int(price)
            self.shopping_list.append({'id': next(self.id_name), 'name': name, 'price': price})
            self.write()
            print(self.shopping_list)
        else:
            input('price must be a number')

    def search(self):
        keys = ['id', 'name', 'price']
        for i, value in enumerate(keys):
            print(f'{i} - {value}')

        choice = int(input('По чому шукатимемо?'))
        sch = input('search...')

        for item in self.shopping_list:
            if str(item[keys[choice]]) == sch:
                print(item)


    def max_shopping_list(self):
        max_price = []
        for ch in self.shopping_list:
            price = ch.get('price')
            max_price.append(price)
        print(max(max_price))

    def menu(self):
        while True:
            print('1) вивід всіх покупок')
            print('2) додавати покупку в книгу')
            print('3) шукати по будь якому полю покупку')
            print('4) показати найдорожчу покупку')
            print('5) видаляти покупку по id')
            print('6) вихід')

            choice = input('make your choose: ')

            match choice:
                case '1':
                    self.show()
                case '2':
                    self.add()
                case '3':
                    self.search()
                case '4':
                    self.max_shopping_list()


s = ShoppingBook('shopping_list.json')
s.menu()
