# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка.
# Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.

from math import ceil


def next_val(x_str, func):
    x = list(map(int, x_str.split(",")))
    res = func(x[-3], x[-2], x[-1])
    return res


def plus_n(a, b, c):
    if c - b == b - a:
        return c + c - b


def multiply_n(a, b, c):
    if c / b == b / a:
        return int(c * c / b)


def degree2_n(a, b, c):
    a = a ** 0.5
    b = b ** 0.5
    c = c ** 0.5
    if c - b == b - a:
        return int(c + 1) ** 2


def degree3_n(a, b, c):
    a = ceil(a ** (1. / 3))
    b = ceil(b ** (1. / 3))
    c = ceil(c ** (1. / 3))
    if c - b == b - a:
        return int(c + 1) ** 3


user_seq1 = '0,2,4,6,8,10'
user_seq2 = '1,4,7,10,13'
user_seq3 = '1,2,4,8,16,32'
user_seq4 = '1,3,9,27'
user_seq5 = '1,4,9,16,25'
user_seq6 = '1,8,27,64,125'

print(next_val(user_seq1, plus_n))
print(next_val(user_seq2, plus_n))
print(next_val(user_seq3, multiply_n))
print(next_val(user_seq4, multiply_n))
print(next_val(user_seq5, degree2_n))
print(next_val(user_seq6, degree3_n))


# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, добутком яких чисел він є.

def palindrom(x):
    x_str = list(str(x))
    if x_str[::-1] == x_str:
        return x


def max_multiply_is_palindrom(a, b):
    res = 0
    res_a = 0
    res_b = 0

    for j in range(a, 0, -1):
        for i in range(b, 0, -1):
            if j * i > res:
                if palindrom(j * i):
                    res = j * i
                    res_a = j
                    res_b = i
    return f'{res} найбільший поліндром для чисел {res_a} i {res_b} в діапазоні {a, b} '


print(max_multiply_is_palindrom(999, 999))
