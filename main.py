# name = "akdil"
# email = "akdilkydykbaev5@gmail.com"
#
# print(name + " " + "akdilkydykbaev5@gmail.com" )
#
# number = 5
# number_2 = 30
# print(number + number_2)
# number_3= 2.2
# print(number_3)
# number_4 =5
# print(number_4 >= 8)
#
#
#
# number = 5
# number_2 = 30
# print(number + number_2)
# number_3 = 2.2
# print(number_3)
# number_8 = 55 / 5
# print(number_8)
# number_4 =5
# print(number_4 == 8)
# number_9 = 1
# print(number_9 == 1)
# surname = "Cristiano"
# name = "Ronaldo"
# print(surname + " " + "Ronaldo"  )
# num = ( 1000/ 7 )
# print(num)
# num=142.85714285714286
# print( 142.85714285714286 % num)
#
# #
# num = int(input("sAn jaz: "))
# num2 = int(input("sAn jaz: "))
# print(num >= num2)
# print("_________________________________________________________________")
# print("-----------------------------------")
# # 8;
# s = "Hello world"
# reversed_s = ''.join(reversed(s))
# print(reversed_s)

# s = "hello world python"
# # split first
# a = s.split()
# # reverse list
# a.reverse()
# # now join them
# result = " ".join(a)
# # print it
# print(result)
#
# #
# #


# for s in range(5,201,5):
#     print(s)

# hi = "akdil"
# for v in hi:
#     print(v)

# for a in "fhhnrtyh":
#     print(a, end="@")

# n = 1
#
# while n <= 20:
#     if n == 5:
#         print(n)
#         continue
# n = 1
# while n < 4:
#     print(f"n (n)")
#     n = n +1
#     print("ghhhh")

# a = 0
# while a < 5:
#     print("hello")
#     a = a + 1
#
#
# number = 11
# for v in range(number):
#     print(v)







# n = int(input('Введите n: '))
# for i in range(1, 11):
#     print(f'{n} * {i} = {n*i}')








# x = 3
# while x * 10:
#     for s in range(1, 11):
#         print(f'{x} * {s} = {x*s}')







# 4;
#
# while True:
#     num = int(input("Введите число: "))
#     if num == 0:
#         break
#     result = num * num
#     print(result)
#
# print("Конец последовательности")






#
# n = "hello"
#
# while n <= 'hello':
#     print(n, end=" ")







# def num(*sam):
#     print(sam)
#
# num("akdil","azamat","danil")












# def filter_odd_num(in_num):
#     if(in_num % 2) == 0:
#         return True
#     else:
#         return False
#
# s = filter_odd_num(451)
# print(s)

















# numbers = [1, 2, 4, 5, 7, 8, 10, 11]
#
# # функция, которая проверяет числа
# def filter_odd_num(in_num):
#     if(in_num % 2) == 0:
#         return True
#     else:
#         return False
#
# # Применение filter() для удаления нечетных чисел
# out_filter = filter(filter_odd_num, numbers)
#
# print("Тип объекта out_filter: ", type(out_filter))
# print("Отфильтрованный список: ", list(out_filter))
# if numbers >= in_num:
#     print(numbers)
# else:
#     print("no")



















# 12:
import time


# def celsius_time(celsius):
#     return (celsius * 7 / 3) + 35
#
# def fahrenheit_time(fahrenheit):
#     return (fahrenheit - 35) * 3 / 7
#
# def timer():
#     print("Выберите преобразование:")
#     print("1. Цельсий в Фаренгейт")
#     print("2. Фаренгейт в Цельсий")
#
#     name = input("Введите номер (1 или 2): ")
#
#     if name == '1':
#         c = float(input("Введите температуру в Цельсии: "))
#         fahrenheit = celsius_time(c)
#         print(f"{c:.2f}°C равно {fahrenheit:.2f}°F")
#
#     elif name == '2':
#         f = float(input("Введите температуру в Фаренгейте: "))
#         celsius = fahrenheit_time(f)
#         print(f"{f:.2f}°F равно {celsius:.2f}°C")
#
#     else:
#         print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
#
#
# if __name__ == "__main__":
#     timer()




















import time
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Запоминаем время до выполнения функции
#         result = func(*args, **kwargs)  # Выполняем функцию
#         end_time = time.time()  # Запоминаем время после выполнения функции
#         execution_time = end_time - start_time  # Вычисляем время выполнения
#         print(f"Время выполнения функции '{func.__name__}': {execution_time:.6f} секунд")
#         return result  # Возвращаем результат выполнения функции
#     return wrapper
#
# # Пример использования декоратора
# @measure_time
# def example_function(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total
#
# # Вызываем функцию
# result = example_function(100)
# print("Результат:", result)














# def order_notification(func):
#     def wrapper(*args, **kwargs):
#         print("Начинаем обработку заказа.")
#         result = func(*args, **kwargs)  # Выполняем переданную функцию
#         print("Обработка заказа завершена.")
#         return result
#     return wrapper
#
# @order_notification
# def create_order(customer_name, product):
#     return f"Заказ для клиента '{customer_name}' товар '{product}' успешно создан."
#
# # Вызовем функцию и проверим вывод
# order_message = create_order("Madara", "")
# print(order_message)


# if i not in store_items:
#     print("Товар не найден. Пожалуйста, выберите другой товар.")
#     continue


