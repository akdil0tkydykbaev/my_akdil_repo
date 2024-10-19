# with open("students.txt", "w") as file:
#     file.write("akdil 89\nayana 96\nmirbek 89")
#     print("Файл записан")

# with open("students.txt", "r") as file:
#     a = file.read()
#     print(a)

# with open("students.txt", "a") as file:
#     file.write("\nБибигул 69")
# print("Файл изменен")

# with open("students.txt", "r") as file:
#     for i in file:
#         print(i)


# with open("students.txt", "w") as file:
#     file.write("mederbek 80\nzamirbek 91\nainazik 85")
#     print("Файл записан")



# ----------------------------------------------------------------------------------------------


# def student(namefile):
#     with open(namefile, 'w') as file:
#
#             name1 = input("Введите имя студента: ")
#             grade1 = input("Введите оценку студента: ")
#             name2 = input("Введите имя студента: ")
#             grade2 = input("Введите оценку студента: ")
#             name3 = input("Введите имя студента: ")
#             grade3 = input("Введите оценку студента: ")
#
#             file.write(f"{name1}, {grade1}\n{name2}, {grade2}\n{name3}, {grade3}\n")
#             print(f"Информация о студентах {name1}, {name2}, {name3}")
#
# namefile = "students.txt"
# student(namefile)
# print(f"Информация о студентах записана в файл {namefile}.")


# def n():
#     with open("students.txt", "w") as file:
#         file.write("akdil 89\nayana 96\nmirbek 89")
#         print("Файл записан")
# n()

# def r(f):
#     with open(f, "r") as file:
#         a = file.read()
#         print(a)
#
# f = "students.txt"
# r(f)

# def append(s):
#     with open(s, "a") as file:
#         file.write("\nБибигул 69")
#         print("Файл изменен")
#
# s = "students.txt"
# append(s)
#
# def forin(b):
#     with open(b, "r") as file:
#         for i in file:
#             print(i)
#
#
# b = "students.txt"
# forin(b)
#
# def writt(x):
#     with open(x, "w") as file:
#         file.write("Akdil 89\nAyana 96\nMirbek 89")
#         print("Файл записан")
#
# x = "students.txt"
# writt(x)
#
# def readd(z):
#     with open(x, "a+") as file:
#         file.write("\nAyana 96")
#         print("Файл изменен")
#
# z = "students.txt"
# readd(z)


# -------------------------------------------------------------


