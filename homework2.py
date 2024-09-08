from typing import Callable


# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання


# def notebook()-> tuple[Callable[[str], None], Callable[[], list[str]]]:
#     l: list[str] = []
#
#     def add_todo(todo: str)-> None:
#         nonlocal l
#         l.append(todo)
#
#     def return_list()-> list[str]:
#         nonlocal l
#         return l.copy()
#
#     return add_todo, return_list
#
# list1 = notebook()
# list2 = notebook()
#
# add1, return1 = list1
# add2, return2 = list2
#
# add1('12312sad')
# add1('12312sad')
# add1('12312sad')
# add2('zzzzzzzzzzzzzzzzzzzzzz')
# add2('zzzzzzzzzzzzzzzzzzzzzz')
# add2('zzzzzzzzzzzzzzzzzzzzzz')
#
# print(return1())
# print(return2())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
#
# def expanded_form(num: int)-> str:
#     string = str(num)
#     length = len(string)-1
#     res = []
#
#     for i, ch in enumerate(string):
#         print(i, ch)
#         if ch != '0':
#             res.append(ch+'0'*(length-i))
#
#     return ' + '.join(res)
#
# print(expanded_form(70304))


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

# def decor(func):
#     counter = 0
#     def inner():
#         nonlocal counter
#         counter += 1
#         func()
#         print(f'count: {counter}')
#
#     return inner
# @decor
# def func():
#     print('func')
#
# func()
# func()
# func()
# func()