# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

# class Rectangle:
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#         self.area = y * x
#
#     def __add__(self, other):
#         return self.area + other.area
#
#     def __sub__(self, other):
#         return self.area - other.area
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.area < other.area
#
#     def __gt__(self, other):
#         return self.area > other.area
#
#     def __len__(self):
#         return self.x + self.y
#
#
# rectangle1 = Rectangle(2, 3)
# rectangle2 = Rectangle(4, 3)
#
#
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 < rectangle2)
# print(rectangle1 > rectangle2)
# print(len(rectangle1))
# print(len(rectangle2))


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:

    def __init__(self, name, age):
        self.age = age
        self.name = name


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.count += 1

    @classmethod
    def snow_count(cls):
        print(cls.count)


class Prince(Human):
    def __init__(self, name, age, shoes_size):
        super().__init__(name, age)
        self.shoes_size = shoes_size

    def search_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if self.shoes_size == cinderella.foot_size:
                print(cinderella.name)


cinderellas: list[Cinderella] = [Cinderella('Drizella', 20, 40), Cinderella('Anastasia', 21, 45), Cinderella('Cinderella', 18, 36)]

prince_charming = Prince('Prince charming', 23, 36)
prince_charming.search_cinderella(cinderellas)

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def printer(self):
        pass


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def printer(self):
        print(self.name)


class Magazine(Printable):

    def __init__(self, name):
        self.name = name

    def printer(self):
        print(self.name)


# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
# класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу


class Main:
    printable_list: list[Book, Magazine] = []

    @classmethod
    def add(cls, other):
        if isinstance(other, Book) or isinstance(other, Magazine):
            cls.printable_list.append(other)

    @classmethod
    def show_all_books(cls):
        for ch in cls.printable_list:
            if isinstance(ch, Book):
                ch.printer()

    @classmethod
    def show_all_magazines(cls):
        for ch in cls.printable_list:
            if isinstance(ch, Magazine):
                ch.printer()


book1 = Book('Prince')
book2 = Book('Princes')

Main.add(book1)
Main.add(book2)

magazine1 = Magazine('Fashion')
magazine2 = Magazine('Garden')

Main.add(magazine1)
Main.add(magazine2)

Main.show_all_books()
print('-------------------------------------------')
Main.show_all_magazines()
