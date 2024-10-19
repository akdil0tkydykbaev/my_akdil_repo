# def hello_world(n):
#     if n % 2 == 0:
#         print(n ** 2)
#     else:
#         print("Oшибка")
#
# hello_world(8)
from itertools import count


# 1:
# def world(n,n1):
#     print(n + n1)
#
# world(5, 8)
# 2:
# def New_York(a, s):
#     if a > s:
#         print(s)
#     else:
#         print(a)
#
# New_York(7,8)
# 3:
# def Russia(d):
#     print(len(d))
#
# Russia("akdil kydykbaev")
#
# 4:
# def Real_Madrid(c, v, b,):
#     print(c + v + b)
# Real_Madrid(5, 3,1)
# 5:
# def akdil(a):
#     print(a ** 2)
# akdil(8)
# 6:
# def  sum_up_to(n):
#     s = 1
#     for d in range(1,):___________________________________________________________________________________________________
#         print(d)
#
# sum_up_to(9)
# 7:
# def factorial(n):
#     factorial = 1
#     while n > 1:
#         factorial *= n
#         n -= 1
#
#     print(factorial)
# factorial(5)
# 8:
# def word_and_symbol(word, symbol):
#     i = 0
#     while i < len(word):
#         print(word[i] * symbol)
#         i += 1


#
#

#

# 10;
# def count_symbol(word, symbol):
#     print(word.count(symbol))
#
# count_symbol("python", "p")
# -------------------------------------------

# def num(*sam):
#     print(sam)
#
# num("akdil","azamat","danil")




# def factorial(n):
#     for i in range(1, n):
#         n *= i
#     return n
#
#
# print(factorial(5))
#





#
# def factorial_while(n):
#     factorial = 1
#     i = 1
#     while i <= n:
#         factorial *= i
#         i += 1
#     return factorial
#
#
# print(factorial_while(5))
#





#
# def word_and_symbol(word, symbol):
#     i = 0
#     while i < len(word):
#         print(word[i] * symbol)
#         i += 1
#
#
# word_and_symbol("python", 10)
#







# def word_and_symbol2(word, symbol):
#     for i in range(len(word)):
#         print(word[i] * symbol)
#
#
# word_and_symbol2("python", 3)






#
# def word_and_symbol(word, symbol):
#     i = 0
#     is_in_symbol = False
#     while i < len(word):
#         if symbol in word:
#             is_in_symbol = True
#         i += 1
#     print(is_in_symbol)
#
#
# word_and_symbol("python", "M")






#
#
# def count_symbol(word, symbol):
#     return word.count(symbol)
#
#
# print(count_symbol("ppythoon", "p"))




#
#
# def main():
#     say_hello()
#     say_goodbye()
#
#
# def say_hello():
#     print("Hello")
#
#
# def say_goodbye():
#     print("Good Bye")
#
#
# # Вызов функции main
# main()







# def say_hello(name="Ainazik", age=18):
#     print(f"Hello, {name}")
#     print(f"You are {age} years old")
#
#
# say_hello("Nursultan", 21)
# say_hello("Sara", 30)



# def print_person(name, age):
#     print(f"Name: {name}  Age: {age}")
#
#
# print_person(age=25, name="John")








#
# def print_person(*, name, surname, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#     print(surname)
#
#
# print_person(name="Bob", surname="Smith", age=41, company="Microsoft")








#
#
# def print_person(name, surname, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", 18, company="Google",)  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", "assd",company="Microsoft", age=42)








#
# def num(*number):
#     cun = 100
#     for i in number:
#         print(cun)
#         cun += i
#         print(cun)
#
# num(1,2,3,3,4,5,)








# def summ_numbers():
#     return 2 + 3
#
# resultat = summ_numbers()
# print(resultat)
#
# if resultat == 4:
#     print("Верно")
# else:
#     print("Неверно")








# def numbers(number, number2):
#     return f"{number} + {number2} = {number + number2}"
#
#
# res = numbers(2, 2)
# print(res)











































































