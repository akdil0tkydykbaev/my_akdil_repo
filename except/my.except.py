# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления:", number1/number2)
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     print(my_list[10])
# except ValueError:
#     print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# except BaseException:
#     print("Общее исключение")
# finally:
#     print("Блок try завершил выполнение")

# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите первое число: "))
#     print("Результат деления:", a / b)
# except ValueError as e:
#     print("Преобразование прошло неудачно",e)
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль",e)


# numbers = input("Введите список чисел, разделенных пробелами: ").split()
# a = 0
# for i in numbers:
#     try:
#         a += int(i)
#     except ValueError:
#         print("Преобразование прошло неудачно", i)
# print(a)


# try:
#     a = int(input("Введите первое число:"))
#     b = int(input("Введите первое число: "))
#     try:
#         n = a / b
#         print(n)
#     except ZeroDivisionError:
#         print("Попытка деления числа на ноль")
# except ValueError:
#     print("Преобразование прошло неудачно")


# 2;
# users = {
# "madara": "1738201229392",
# "saske": "43y75767653e",
# "sunade": "2w0w4ew9jfnshw",
# }
#
# def work():
#     while True:
#         try:
#             a = input("Введите логин: ")
#             b = input("Введите пароль: ")
#             if a in users:
#                 if users[a] == b:
#                     print("Успешный вход!")
#                     break
#                 else:
#                     print("Неверный логин или пароль. Попробуйте снова.")
#
#         except Exception as e:
#             print("Произошла ошибка", e)
# work()


# 3;
# shop = {
#     "меч": 150,
#     "щит": 100,
#     "зелье": 50,
# }
#
#
# # v = 500
# def buy_item():
#     v = 500
#     while True:
#         try:
#             i = input("Введите название товара: ").lower()
#
#             if i == 'выход':
#                 print("Спасибо за покупку!")
#                 break
#             try:
#                 a = int(input(f"Введите количество товара '{i}': "))
#                 if a <= 0:
#                     raise ValueError("Количество должно быть положительным.")
#             except ValueError as e:
#                 print(e)
#                 continue
#             b = shop[i] * a
#
#             if b > v:
#                 print("У вас недостаточно средств для этой покупки.")
#             else:
#                 v -= b
#                 print(f"Вы купили {a} '{i}' на сумму {b}. Оставшийся бюджет: {v}")
#         except Exception as e:
#                 print(e)
#
# buy_item()

# def get_student_data():
#     while True:
#         try:
#             name = input("Введите имя студента: ")
#             if not name.isalpha():
#                 raise ValueError("Имя должно содержать только буквы.")
#
#             age = int(input("Введите возраст студента: "))
#             if age <= 0:
#                 raise ValueError("Возраст должен быть положительным целым числом.")
#
#             phone = input("Введите номер телефона студента: ")
#             if not phone.isdigit():
#                 raise ValueError("Номер телефона должен содержать только цифры.")
#
#             print("Данные студента успешно зарегистрированы!")
#             return name, age, phone
#
#         except ValueError as e:
#             print(e)
#
# student_data = get_student_data()
# print(f"Имя: {student_data[0]}, Возраст: {student_data[1]}, Номер телефона: {student_data[2]}")

# def check_password_strength(password):
#     while True:
#         if len(password) < 8:
#             raise