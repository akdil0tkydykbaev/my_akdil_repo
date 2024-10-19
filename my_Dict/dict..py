# from idlelib.debugger_r import restart_subprocess_debugger
#
#
# def my_decorator(func):
#
#     def wrapper():
#         print("hello")
#         resultat = func()
#         print("bye")
#         return resultat
#     return wrapper
#
# @my_decorator
# def mu_func():
#     print("my_function")
#
# mu_func()
# n = my_decorator(mu_func)
# n()
from multiprocessing.resource_tracker import register
from turtledemo.penrose import start


# def my_dict(fun):
#
#     def num():
#         print("start ocnovnoi func")
#         resultat = fun()
#         print("cones ocnovnoi func")
#         return resultat
#     return num
#
#
# @my_dict
# def sun():
#     print("akdil")
#
# sun()



# def wip(see):
#
#     def smena_ava():
#         print("register")
#         print("lodin")
#         resultat = see()
#         print("vyti")
#         return resultat
#     return smena_ava
# @wip
# def sun():
#     print("ava coshtum")
#
# sun()

#
# def game(plya):
#     def wrapper():
#         start()
#         num = plya()
#         cones()
#         return num
#     return wrapper
#
# @game
# def levl():
#     print("levl 1")
#
# @game
# def ochko():
#     print("ochko 0")
#
# @game
# def ochco():
#     print("ochco 100")
#
# @game
# def level():
#     print("levl 10")
#
# def start():
#     print("start")
#
# def cones():
#     print("cones")
#
# levl()
# ochko()
# ochco()
# level()


# def num(func):
#     def pon():
#         start_session()
#         sun = func()
#         stop()
#         return sun
#     return pon
#
# @num
# def session():
#     print("dobavid tovar")
#
# @num
# def sess():
#     print("ybrat tovar")
#
#
# def start_session():
#     print("start")
#
# def stop():
#     print("stop")
#
#
# session()
# sess()




# import time
# def measure_time(function):
#     def wrapper():
#         start = time.time()
#         res = function()
#         end = time.time()
#         work = end - start
#         print(f"Время выполнения работы: {work}")
#         return res
#     return wrapper
# @measure_time
# def example():
#     time.sleep(5)
# ayan = example()
# print(ayan)


# 2;
# def calculator(func):
#     def wrapper(*args):
#         start()
#         result = func(*args)
#         print(f"Результат операции: {result}")
#         end()
#         return result
#     return wrapper
#
# @calculator
# def add(a, b):
#     return a + b
#
# @calculator
# def subtract(a, b):
#     return a - b
#
# @calculator
# def multiply(a, b):
#     return a * b
#
# @calculator
# def divide(a, b):
#     if b == 0:
#         return "Ошибка:"
#     return a / b
#
# def start():
#     print("Старт работы калькулятора.")
#
# def end():
#     print("Завершение работы калькулятора.\n")
#
#
# result_add = add(10, 5)
# result_subtract = subtract(10, 5)
# result_multiply = multiply(10, 5)
# result_divide = divide(10, 0)
# result_divide_valid = divide(10, 5)

# 3;
# def order_notification(func):
#     def wrapper(*names, **product):
#         start()
#         end()
#         res = func(*names, **product)
#         return res
#     return wrapper
#
# # @order_notification
# # def zacachik():
# #     print(f"Заказ клиента '{names}' готов .")
# #
# # @order_notification
# # def product():
# #     print(f"товар '{product}' успешно создан.")
#
# @order_notification
# def create_order(customer_name, product):
#     return f"Заказ для клиента '{customer_name}' товар '{product}' успешно создан."
#
# def start():
#     print("Начинаем обработку заказа.")
#
# def end():
#     print("Обработка заказа завершена.")
#
#
# order_message = create_order("Madara", "Шаринган")
# print(order_message)







# 1;
# def game(func):
#     def wrapper(*args):
#         print("началa хода.")
#         log_turn()
#         res = func(*args)
#         print("завершении хода.")
#         return res
#     return wrapper
#
# def  log_turn():
#     print("ACTA начинает ход.")
# @game
# def attac(character_name,enemy_name,damage):
#     print(f"'{character_name}' атакует '{enemy_name}'")
#     print(f"'{enemy_name}'  получает '{damage}' уронов")
#
# attac("ACTA","GON","70")

# 3;
# def log_turn(func):
#     def wrapper(character_name, enemy_name, damage):
#         print(f"ход начинает персонаж '{character_name}' ")
#         print(f"Персонаж '{character_name}' атакует '{enemy_name}' силой {damage} ")
#         result = func(character_name, enemy_name, damage)
#         end()
#         return result
#     return wrapper
#
# @log_turn
# def attack(character_name, enemy_name, damage):
#     print(f"персонаж '{enemy_name}' получил {damage} урона ")
#
# def end():
#     print("Ход завершен ")
#
# attack("сайтама", "гароу", 99999999999999)


# 2;
# def log_turn(func):
#     def wrapper(character_name, enemy_name, damage):
#         res = func(character_name, enemy_name, damage)
#         print(f"персонаж '{enemy_name}' получил '{damage}' урона")
#         end()
#         return res
#     return wrapper
#
#
# @log_turn
# def attacc(character_name, enemy_name, damage):
#     print(f"Персонаж '{character_name}' атакует '{enemy_name}' силой {damage}")
# @log_turn
# def attack( enemy_name, damage):
#     print(f"персонаж '{enemy_name}' получил '{damage}' урона")
#
# def start(*character_name):
#     print(f"ход начинает персонаж '{character_name}'")
#
# def end():
#     print("Ход завершен")
#
#
# start("сайтама")
# attacc("сайтама","гароу",70)
# attack("гароу", 50 )
# end()

















































