# i = 10000000000000000
# while i > 10:
# #     i -= 1000000
# #     print(i)
#
#
# def add(func):
#     def aa():
#         hello()
#         res = func()
#         good_bya()
#         return res
#     return aa
#
# @add
# def dd():
#     print("my name is Akdil")
#
# def hello():
#     print("heloo")
#
# def good_bya():
#     print("good bya.")
from os import times
from turtledemo.penrose import start


# dd()

# def sss(tab):
#     def war(*names):
#         print("cabak bashtaldi")
#         res = tab(*names)
#         print("cabak bytty")
#         return res
#     return war
#
# @sss
# def nun(name, surname):
#     print(f"тема урока 'lambda' учител {name} {surname}")
#
#
# nun("jony","bahtiyar")


#
# def pain(times):
#     def obiti(func):
#         def momoshiki(*args):
#             for i in range(times):
#                 print(f"vyzyv {i+1}")
#                 res = func(*args)
#                 print(res)
#         return momoshiki
#     return obiti
#
# @pain(2)
# def mage(name):
#     return f"hello, {name}!"
#
# mage("akdil")
# #
# def repeat(times):
#     def decorator(func):
#         def wrapper(*args):
#             for i in range(times):
#                 print(f"Вызов {i+1}:")
#                 result = func(*args)
#                 print(result)
#         return wrapper
#     return decorator
# #
# #
# @repeat(3)
# def greet(name):
#     return f"Привет, {name}!"

# greet("Akdil")



# --------------------------------------------------------------------------------------------------------------------



# 1;
# def log_turn(func):
#     def wrapper(character_name,enemy_name,damage):
#
#
#         res = func(character_name,enemy_name,damage)
#         print("завершении хода.")
#         return res
#     return wrapper
#
# def  attack(*character_name):
#     print(f"ход начинает персонаж '{character_name}'")
# attack("ACTA")
# @log_turn
# def attac(character_name,enemy_name,damage):
#     print(f"'{character_name}' атакует '{enemy_name}'")
#     print(f"'{enemy_name}'  получает '{damage}' уронов")
#
# attac("ACTA","GON","70")

# 2;
# def log_turn(func):
#     def wrapper(character_name, enemy_name, damage):
#         print(f"ход начинает персонаж '{character_name}' ")
#         print(f"Персонаж '{character_name}' атакует '{enemy_name}' силой {damage} ")
#         result = func(character_name, enemy_name, damage)
#         print("Ход завершен ")
#         return result
#     return wrapper
#
# @log_turn
# def attack(character_name, enemy_name, damage):
#     print(f"персонаж '{enemy_name}' получил {damage} урона ")
#
# # def end():
# #     print("Ход завершен ")
#
# attack("сайтама", "гароу", 999)


# 3;
# def log_turn(func):
#     def wrapper(character_name, enemy_name, damage):
#         res = func(character_name, enemy_name, damage)
#         print(f"персонаж '{enemy_name}' получил '{damage}' урона")
#         end()
#         return res
#     return wrapper
#
# @log_turn
# def attacc(character_name, enemy_name, damage):
#     print(f"Персонаж '{character_name}' атакует '{enemy_name}' силой {damage}"

# # @log_turn
# # def attack( enemy_name, damage):
# #     print(f"персонаж '{enemy_name}' получил '{damage}' урона")
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



































#
#
def log_turn(func):
    def wrapper(character_name, enemy_name,damage):
        print(f"Персонаж '{character_name}' атакует '{enemy_name}' ")
        print(f"'{enemy_name}' уклонился от атаки '{character_name}'")
        result = func(character_name, enemy_name,damage)
        print(f" c огромной силой '{enemy_name}' ударил '{character_name}' ")
        print(f"'{character_name}' получил '{damage}' урона ")
        print(f"после атаки '{enemy_name}'        '{character_name}'  не может встать")
        print(f"чтооооооооо  '{character_name}'   он встал не может быть ????? как?????????  после такой атаки ")
        print(f"да '{character_name}' встал  битва продалжается")
        print("Ход завершен ")
        return result
    return wrapper

@log_turn
def attack(character_name,enemy_name,damage):
    print(f"'{enemy_name}' очень силён ")

attack("сон гоку","жиран","99999999999999")


















