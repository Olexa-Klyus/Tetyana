import module_student
import module_group
import logger_Info

if __name__ == "__main__":
    try:
        logger_Info.logger.info("Started logging")
        group = module_group.Group("group", max_group=10)
        group.add_student(module_student.Student("Lida", "Vasylenko", 25))  # 1
        group.add_student(module_student.Student("Oksana", "Dovzhenko", 20))  # 2
        group.add_student(module_student.Student("Yurii", "Kozak", 26))  # 3
        group.add_student(module_student.Student("Denys", "Zhuk", 29))  # 4
        group.add_student(module_student.Student("Olha", "Nesterenko", 32))  # 5
        group.add_student(module_student.Student("Ostap", "Stelmakh", 18))  # 6
        group.add_student(module_student.Student("Marta", "Buriak", 23))  # 7
        group.add_student(module_student.Student("Hanna", "Shepit", 35))  # 8
        group.add_student(module_student.Student("Serhii", "Haiduk", 22))  # 9
        # group.add_student(module_student.Student("Andrii", "Melnyk", 19))   # 10
        # group.add_student(module_student.Student("Ivan", "Horyn", 21))

        res_find = group.find_student("Nesterenko")
        for item in res_find:
            print(item)
        for item in res_find:
            print(item.name, item.surname, item.age, sep="_")
        print(group)
        logger_Info.logger.info("Finished logging")

    except Exception as error:
        print(error)
