# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому?
#
# st = 'w123fasdv7698'
#
# nums =[]
#
# for num in st:
#     if num.isdigit():
#         nums.append(num)
#     else: continue
# print(', '.join(nums))
from idlelib.colorizer import prog_group_name_to_tag

# 2) написати прогу яка вибирає зі введеної строки числа і виводить їх так як вони написані

# st = 'as 23 fdfdg544 34'
#

# nums = []
#
# for num in st:
#     if num.isdigit():
#         nums.append(num)
#     else: nums.append(' ')
# print(', '.join((''.join(nums)).split()))

# list comprehensions


# 3)є строка greeting. записати кожний символ як окремий елемент списку і зробити його заглавним:
# greeting = 'Hello, world'
# ch = (''.join(i for i in greeting)).upper() ## frst var
# print([i for i in ch])

# print([ch.upper() for ch in greeting]) ## sec var


# 4) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# i = 0
# print(i)
# while i < 50:
#     i += 1
#     if i % 2 != 0:
#         print(i**2)

# print([i**2 for i in range(50) if i % 2])


# functions

# - створити функцію яка виводить ліст

# def show_list(li):
#     for i in li:
#         print(i)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_numer (a, b, c):
#     max_num = max(a, b, c)
#     print(max_num)
#     return max_num
#
# max_numer(2, 11, 8)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def max_min_nums(*args):
#     min_args = min(args)
#     max_args = max(args)
#     print(max_args)
#     return min_args
#
# max_min_nums(1, 4, 87)

# - створити функцію яка повертає найбільше число з ліста

# l = [1, 5, 12, 8, 52, 2]
#
# def max_num_of_list(l):
#     return max(l)
# max_num_of_list(l)

# - створити функцію яка повертає найменьше число з ліста

# def min_num_of_list(l):
#     return min(l)
# min_num_of_list(l)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


# def sum_nums(l):
#     return sum(l)
# sum_nums(l)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def func(l):
#     return sum(l)/len(l)
#
# func(l)



# 1)Дан list:
l = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
# def min_list_num(l):
#     return min(l)
# min_list_num(l)

#   - видалити усі дублікати

# set = set(l)
# print(set)

#   - замінити кожне 4-те значення на 'X'

def change_to_x(l):
    print()



# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню


