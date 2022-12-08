# # 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому
#
# s = input("text: ")
# c = [item for item in s if item.isdigit()]
# print(', '.join(c))
#
#
# # 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# # так як вони написані
# # наприклад:
# #   st = 'as 23 fdfdg544 34' #введена строка
# #   23, 544, 34              #вивело в консолі
#
# s = input("text: ")
# for item in s:
#     if not item.isdigit():
#         s = s.replace(item, "  ")
# while "  " in s:
#     s = s.replace("  ", " ")
# s = s.replace(" ", ",")
# print(s)

# мій варіант
# s = input("text: ")
# for item in s:
#     if not item.isdigit():
#         s = s.replace(item, " ")
# ls = s.split()
# print(", ".join(ls))

# варіант викладача
# st = input("text: ")
# print(', '.join("".join([i if i.isdigit() else " " for i in st]).split()))
#


# # 1)є стрічка:
# # greeting = 'Hello, world'
# # записати кожен символ у список, змінивши регістр на верхній
#
# s = "Hello, world"
# c = [item.upper() for item in s]
# print(c)
#
#
# # 2) з діапазону 0-50 записати у список тільки непарні числа, піднісши їх до квадрату,
# # напр.:
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
# c = [item ** 2 for item in range(0, 51)]
# print(c)
#
# # створити функцію, яка виводить ліст
# def create_list(s):
#     print(list(s))
#
# create_list("45673563956394")
#
# # створити функцію, яка приймає три числа, виводить та повертає найменше.
#
#
# def min_num(a, b, c):
#     res = min(a, b, c)
#     print(res)
#     return res
#
#
# min_num(7, 567, 43)
#
# # створити функцію, яка приймає три числа, виводить та повертає найбільше.
#
#
# def max_num(a, b, c):
#     res = max(a, b, c)
#     print(res)
#     return res
#
#
# max_num(7, 567, 43)
#
#
# # створити функцію, яка приймає будь-яку кількість чисел, повертає найменше, а виводить найбільше
#
#
# def num_1(x):
#     res_min = min(x)
#     res_max = max(x)
#     print(res_max)
#     return res_min
#
#
# s = input("n: ")
# s = s.split(",")
# s = list(map(int, s))
# num_1(s)
#
# # створити функцію, яка повертає найбільше число з ліста
#
# def max_list(y):
#     res = max(y)
#     return res
#
#
# list_1 = [2, 3, 0.4, 56, 9]
# print(max_list(list_1))
#
#
# # створити функцію, яка повертає найменше число з ліста
#
#
# def min_list(x):
#     res = min(x)
#     return res
#
#
# list_1 = [2, 7, 56, 0.4, 9]
# print(min_list(list_1))
#
# # створити функцію, яка приймає ліст чисел та складає значення елементів ліста та повертає його
#
# list_x = [257, 77687, 5, 0.4, 967]
#
#
# def sort_list(l):
#     res = sorted(l)
#     return res
#
#
# print(sort_list(list_x))
#
# # створити функцію, яка приймає ліст чисел та повертає середнє арифметичне його значень
#
# list_x = [257, 77687, 77, 5, 967]
#
# def med_list(x):
#     res = sum(x) / len(x)
#     return res
#
# print(med_list(list_x))
#
#
# # 1)Є список:
# # x = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# #   - знайти min число
# #   - видалити дублікати
# #   - замінити кожне четверте значення на "Х"
# # 2) вивести на екран пустий квадрат із "*", сторона якого вказана у змінній:
# # 3) вивести табличку множення за допомогою циклу while
# # 4) переробити перше завдання під меню за допомогою циклу
#
# x = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# # 1)
# print(min(x))
#
# print(list(set(x)))
#
# n = 4
# while n < len(x):
#     x[n] = "*"
#     n += 4
# print(x)
#
# # 2)
# n = 7
# print("*" * n)
# for i in range(n - 2):
#     print("*" + " " * (n - 2) + "*")
# print("*" * n)                             # чому він не схожий на квадрат
#
# # 3)
# i = 1
# while i in range(1, 11):
#     for n in range(1, 11):
#         print(f"{i * n}", end="  ")
#     print()
#     i += 1

# мій варіант
# i = 1
# while i in range(1, 11):
#     for n in range(1, 11):
#         resValue = i * n
#         print(f"{str(resValue) + ' ' if resValue < 10 else resValue}", end="  ")
#     print()
#     i += 1
