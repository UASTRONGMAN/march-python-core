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
#         self.x = x
#         self.y = y
#
#     def area(self):
#         return self.x * self.y
#
#     def len(self):
#         return self.x + self.y
#
# rec1 = Rectangle(1, 2)
# rec2 = Rectangle(2, 3)
# print(rec1.area() + rec2.area())
# print(rec1.area() - rec2.area())
# print(rec1.area() == rec2.area())
# print(rec1.area() != rec2.area())
# print(rec1.area() > rec2.area())
# print(rec1.area() < rec2.area())
# print(rec1.len())
# print(rec2.len())


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Cinderella(Human):
#     count: int = 0
#
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.foot_size = foot_size
#         Cinderella.count += 1
#
#     @classmethod
#     def count_print(cls):
#         return cls.count
#
#     def __str__(self):
#         return str(self.__dict__)
#
# class Prince(Human):
#     arr = []
#     def __init__(self, name, age, hidden_shoes):
#         super().__init__(name, age)
#         self.hidden_shoes = hidden_shoes
#
#
#     def find_love(self, arr: list[Cinderella]):
#         for i in arr:
#             if i.foot_size == self.hidden_shoes:
#                 return i
#
#
#     def __str__(self):
#         return str(self.__dict__)
# arr: list[Cinderella] = [
#     Cinderella('Ann', 23, 36),
#     Cinderella('Sofia', 21, 37),
#     Cinderella('Ksenia', 19, 38),
#     Cinderella('Lola', 16, 35),
#     Cinderella('Kris', 28, 41),
#     Cinderella('Katya', 25, 36)
# ]
#
# prince = Prince('Oscar', 24, 38)
#
# print(prince.find_love(arr))
# print(Cinderella.count_print())



# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде: - змінна класу printable_list яка буде зберігати книжки та журнали - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку
# чи то що передають є класом Book або Magazine инакше ігрнорувати додавання - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу - метод show_all_books
# який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки классів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(user, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This book is {self.name}')

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This magazine is {self.name}')

class Main:
    __printable_list: list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, Book|Magazine):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
Main.show_all_books()