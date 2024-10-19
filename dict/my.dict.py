# student = {
#     "k": "akdil",
#     "r": "ayana",
#     "s": "meder",
# }
#
# for key in student:
#     print(key)
import random
from turtledemo.penrose import start

# fryct = {"alma": "10","anar": "20","malina": "80"}
#
# print(fryct["alma"])

#
# fryct = {"alma": 6,"anar": 20,"malina": 80}
#
# i = fryct["alma"]
#
# if i < 3:
#     print(i + 3)
# else:
#     print(fryct["alma"])


# _______________________________________________________________

# 1;
# def invert_dict(dict):
#     a = {}
#     for key, value in dict.items():
#         a[value] = key
#     return a
#
# s = {1: "a", 2: 's', 3: 'd'}
# b = invert_dict(s)
# print(b)
#
# # 2;
# def dict_to_tuple_list(args):
#     return list(args.items())
#
# args = {'Akdil': 25, 'Fatima': 30, 'Mirbek': 35}
# a = dict_to_tuple_list(args)
# print(a)

# 3;
# def students(args):
#     a = {}
#     b = {}
#     for i, p in args.items():
#         if p >= 80:
#             a[i] = p
#         else:
#             b[i] = p
#     return a, b
#
# args = {
#     'Аяна': 96, 'Акдил': 89, 'Талгарбек': 75, 'Бибигул': 69,
#     'Мирбек': 89, 'Айназик': 81, 'Медербек': 80, 'Кудайберди': 86,
#     'Фатима': 84, 'Замирбек': 91, 'Азамат': 13
# }
#
# a, b = students(args)
# print("Прошли:", a)
# print("Не прошли:", b)






# 1;
# my_dict = {}
# my_dict['name'] = 'John'
# my_dict['age'] = 20
# print(my_dict)
# 2;
# fruits = {'apple':10, 'banana':20, 'orange': 5}
# print(fruits['apple'])
# 3;
# person = {'name':'alice', 'age':30,'city':'New York'}
# print(person['age'])
# 4;
# fruits = {'apple':10, 'banana':20, 'orange': 5}
# print(fruits['banana'] + 2)
# 5;
# fruits = {'apple': 10, 'banana': 20, 'orange': 5}
# key = 'apple'
# if key in fruits:
#     user = fruits[key]
#     print(user)
# 6;
# person = {'name':'alice', 'age':30,'city':'New York'}
# for key in person:
#     print(key)
# 7;
# fruits = {'apple': 10, 'banana': 20, 'orange': 5}
# for v in fruits.values():
#     print(v)
# 8;
# person = {'name':'alice', 'age':30,'city':'New York'}
# for key, value in person.items():
#     print(key, value)
# 9;
# fruits = {'apple': 10, 'banana': 20, 'orange': 5}
# del fruits['orange']
# print(fruits)
# 10;
# my_dict = {'name': 'John'}
# a = my_dict.clear()
# print(a)




# text = " Менин атым Акдил акдил"
#
# def me(text):
#     z = text.lower().split()
#     a = {}
#     for i in z:
#         if i in a:
#             a[i]+=1
#         else:
#             a[i]=1
#     return a
#
# print(me(text))

# list = [1,2,3,4,5]
#
# def dell(list):
#     a = {}
#     for i in list:
#         a[i] = i * i
#     return a
# print(dell(list))





# d1 = {1:10,2:20,3:30,4:40,5:50}
# d2 = {1:10,2:20,3:30,4:40,5:50}
# def number(dict1,dict2):
#     i = dict(dict1)
#     for k,v in dict2:
#         if v == i:
#             a = v+i
#     return a
#
# dict1 = {1:10,2:20,3:30,4:40,5:50}
# dict2 = {1:10,2:20,3:30,4:40,5:50}
# print(number(dict1,dict2))



# import random
#
# # animals = {
# #     'слон': 'Это самое большое наземное животное.',
# #     'тигр': 'Это полосатый хищник.',
# #     'панда': 'Это черно-белое животное, которое ест бамбук.',
# #     'крокодил': 'Это рептилия, которая живет в воде.',
# #     'коала': 'Это сумчатое животное, которое обитает в Австралии.',
# # }
# #
# # def guess_animal_game():
# #     a, b = random.choice(list(animals.items()))
# #
# #     print("Игра; Угадайте животное")
# #     print("Подсказка:", b)
# #
# #     while True:
# #         v = input("Введите ваше предположение: ")
# #
# #         if v.lower() == a:
# #             print("Поздравляем! Вы угадали!")
# #             break
# #         else:
# #             print("Увы, вы не угадали.")
# #             print("Попробуйте еще раз.")
# #
# guess_animal_game()


people = ["Mike", "Bill", "Ted"]

users = set(people)
print(users)



















































































































