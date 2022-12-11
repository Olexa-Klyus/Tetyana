# # 1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.
#
# def function_one(a: int, b: int, w: str):
#     res = a + b
#     return w + str(res)     # рядок +сума чисел
#
#
# print(function_one(3, 5, 'Привіт '))

# варіант ментора
# def func(a, b, c):
#     if isinstance(a, int) and isinstance(b, int):  # це якщо потрібна перевірка але перевірку бажано робити в тілі програми
#         return f'{a + b}{c}'
#     return -1
#
#
# print(func(1, 2, 'hello'))

# 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.

# def stars_rectangle(a, b):
    # res = ""
    # for i in range(b):
    #     res = res + "*" * a
    #     if i < b - 1:  # це щоб останній ентер не доліплявся
    #         res = res + "\n"
    # return res

    # або
    # return (("*" * a + "\n") * b)[:-1]

    # варіант ментора
    # return f'{"*" * b}\n' +\
    #        f'*{" " * (b - 2)}*\n' * (a - 2) + \
    #        '*' * b


# print(stars_rectangle(10, 5))

#
# # 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел. Якщо такий елемент у списку є,
# # то поверніть індекс, якщо ні, то поверніть число «-1».
# x_list = [7, 5, 3, 8, 9, 10, 6, 345]
#
#
# def find_elem(n):
#     if n in x_list:
#         s = x_list.index(n)
#     else:
#         s = -1
#     return s
#
#
# print(find_elem(9))
#
#
# # 4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.
# s = "This is text example"
#
#
# def words_count(s):
#     res = len(s.split())
#     return res
#
#
# print(words_count(s))
#
#
# # 5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# # > 123,34
# # > one hundred twenty three dollars thirty four cents
# from num2words import num2words
#
#
# def numb_into_words(s):
#     n = s.find(".")
#     m = s[:n]
#     v = s[n + 1:]
#
#     res = num2words(m) + " dollars " + num2words(v) + " cents"
#     return res
#
#
# print(numb_into_words("657.84"))


# from num2words import num2words
#
#
# def numb_into_words(s):
#     s = str(s).rpartition('.')
#     res = num2words(s[0]) + " dollars " + num2words(s[2]) + " cents"
#     return res
#
#
# print(numb_into_words(657.84))

#
#
# # 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# # Наприклад: XXII -> 22
#
#
# def rom_to_dec(rom_num):
#     voc = {
#         "I": 1, "V": 5, "IX": 9, "X": 10, "L": 50, "XC": 90, "C": 100, "D": 500, "M": 1000
#         }
#
#     number = 0
#     rom_num = rom_num.replace("IV", "IIII").replace("IX", "VIIII")
#     rom_num = rom_num.replace("XL", "XXXX").replace("XC", "LXXXX")
#     rom_num = rom_num.replace("CD", "CCCC").replace("CM", "DCCCC")
#     for symbol in rom_num:
#         number += voc.get(symbol)
#     return number
#
#
# print(rom_to_dec("IX"))
