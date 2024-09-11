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

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size

    def __str__(self):
        return str(self.foot_size)

class Prince(Human):
    def __init__(self, name, age, hidden_shoes):
        super().__init__(name, age)
        self.hidden_shoes = hidden_shoes

    # @staticmethod
    def find_love(self ,arr):
        return (foot_size for foot_size in arr if foot_size == self.hidden_shoes)

cin1 = Cinderella('Ann', 23, 36)
cin2 = Cinderella('Sofia', 21, 37)
cin3 = Cinderella('Ksenia', 19, 38)
cin4 = Cinderella('Lola', 16, 35)
cin5 = Cinderella('Kris', 28, 41)
cin6 = Cinderella('Katya', 25, 36)

prince = Prince('Oscar', 24, 38)

arr = [cin1.foot_size, cin2.foot_size, cin3.foot_size, cin4.foot_size, cin5.foot_size, cin6.foot_size]
print(arr)