# Написати програму, яка буде повертати для заданого року кількість днів.
# Рік є високосним, якщо він кратний 4, але не кратний 100,
# а також якщо він кратний 400# n = int(input("Enter a year: "))
# year = 365
# # уважно
# # якщо він (кратний 4 та не кратний 100) або (кратний 400)
# if (not n % 4 and n % 100) or not n % 400:
#     year = 366
# print(year)


# Exercise 1
# Є девятиповерховий будинок, в якому 4 під'їзди.
# Номер підїзду починається з одиниці. На одному поверсі - 4 квартири. Напишіть програму,
# яка від користувача отримує номер квартири та виводить для заданої квартири номер підїзду, поверху та номер на поверсі.
# Якщо такої квартира немає в цьому будинку, то необхідно повідомити користувача про це. ( не використовувати if )
# import math

# n = int(input("Flat number is "))
# flat = 4
# stage = 9
# block = flat * stage
# blocks = block * 4
#
# e = math.ceil(float(n / block))
# print(f"Entrance is {e}")
#
# f = math.ceil((n - (e - 1) * block) / flat)
# print(f"Floor is {f}")
#
# o = int((n - (e - 1) * block) - (flat * (f - 1)))
# print(f"Order of the apartment is {o}")
#
# n = 145
# rrr = (1 <= n <= 144) and (f'Номер квартири - {n}')
# print(rrr or ("Such flat doesn`t exist in this building"))

# Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
# Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.


# тернарка
#
# n = 2
# if n == 0:
#     year = 365

# year = 365 if n == 0 else 366
# print(year)

# year = (365, 366, 367)[2]
# print(year)
#
# for i in range(10):
#     print(i)

# text_input = input("Text: ")
# res_word = text_input
# j = 1
#
# while text_input == res_word and j <= len(text_input):
#     part_word = text_input[0:j]
#
#     i = 0
#     while i + 2 * j <= len(text_input):
#
#         if part_word == text_input[i + j:i + 2 * j]:
#             res_word = part_word
#         else:
#             res_word = text_input
#             break
#
#         if i + 2 * j - len(text_input) < 0:
#             res_word = text_input
#
#         i += j
#     j += 1
#
# print(res_word)


