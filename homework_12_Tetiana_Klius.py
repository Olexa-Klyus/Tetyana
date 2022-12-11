# # 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
#
# class Person:
#     def __init__(self, name: str, surname: str, age: str):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def get_inf(self):
#         return f"{self.name} {self.surname}, {self.age} y.o."
#
#     def __str__(self):  # needed for exercise 3
#         return f"{self.name} {self.surname}, {self.age} y.o."
#
#
# person_1 = Person("Hanna", "Shepit", "35")
# print(person_1.get_inf())
#
#
# # 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
#
# class Student(Person):
#     def get_inf(self):
#         return f"{self.name} {self.surname}"
#
#
# person_1 = Student("Hanna", "Shepit", "35")
# print(person_1.get_inf())
#
#
# # 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент. Реалізуйте методи додавання,
# # видалення студента та метод пошуку студента за прізвищем.
# # Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
#
#
# class Group:
#     def __init__(self, title):
#         self.title = title
#         self.group = []
#
#     def add_student(self, student):
#         if student not in self.group:
#             self.group.append(student)
#
#     def remove_student(self, student):
#         if student in self.group:
#             self.group.remove(student)
#
#     def find_student(self, surname):
#         return f"{self.title}, student: {surname}" if surname in '; '.join(map(str, self.group)) else -1
#
#     def __str__(self):
#         return f"{self.title}:\n" + '; '.join(map(str, self.group))
#
#
#
# Вирішення завдання ментором
class Humen:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'


class Student(Humen):

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'{super().__str__()},{self.age}'


class Group:

    def __init__(self, title, max_students=10):
        self.title = title
        self.__students = []
        self.max_student = max_students

    def add_student(self, student):
        if student not in self.__students and len(self.__students) < self.max_student:
            self.__students.append(student)

    def __str__(self):
        return f'{self.title}\n' + '*' * 15 + '\n' + '\n'.join(map(str, self.__students))

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

    def find_student(self, surname):
        res = []
        for student in self.__students:
            if student.surname == surname:
                res.append(student)
        return res


student_1 = Student("Hanna", "Shepit", "35")
student_2 = Student("Serhii", "Haiduk", "22")
student_3 = Student("Andrii", "Melnyk", "19")
student_4 = Student("Oksana", "Dovzhenko", "20")
student_5 = Student("Marta", "Buriak", "23")
student_6 = Student("Lida", "Vasylenko", "25")
student_7 = Student("Yurii", "Kozak", "26")
student_8 = Student("Olha", "Nesterenko", "32")
student_9 = Student("Denys", "Zhuk", "29")
student_10 = Student("Ostap", "Stelmakh", "18")

group = Group("Python")
group.add_student(student_1)
group.add_student(student_2)
group.add_student(student_3)
group.add_student(student_5)
group.add_student(student_8)
group.add_student(student_9)

group.remove_student(student_9)

res = group.find_student("Shepit")
for item in res:
    print(item)
    print(item.name, item.surname, item.age)
res = group.find_student("Buriak")
for item in res:
    print(item)

print(group)
