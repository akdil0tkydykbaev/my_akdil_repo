# number = lambda: print("hello")
# number()
#
#
# # --------------------------
# square = lambda n: n * n
# print(square(5))
#
#
#
# def square(n):
#     return n * n
# print(square(5))
# -------------------------
from list.my_list import numbers

# sum = lambda a, b: a + b
#
# print(sum(4, 5))

# def summa(a, b):
#     return a + b
#
# print(summa(4, 5))
# print(summa(5, 6))
#------------------------------


# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# do_operation(5, 4, lambda a, b: a + b)
# do_operation(5, 4, lambda a, b: a * b)
#----------------------------------------------



# def select_operation(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     else:
#         return lambda a, b: a * b
#
#
# operation = select_operation(1)  # operation = sum
# print(operation(10, 6))  # 16
#
# operation = select_operation(2)  # operation = subtract
# print(operation(10, 6))  # 4
#
# operation = select_operation(3)  # operation = multiply
# print(operation(10, 6))  # 60
# ------------------------------------------------------------------------------------


# def double_or_triple(x):
#     if x % 2 == 0:
#         return lambda : x * 2
#     else:
#         return lambda :x * 3
#
#
#
#
# new = lambda x: x*2 if x % 2 == 0  else x * 3
# print(new(8))




# new = lambda s: len(s) if len(s) > 5 else s[::-1]
# print(new("python"))

# num = lambda a,b: a if a > b else b
# print(num(4,5))

#
# sun = list(filter(lambda i :list( i % 2 == 0



# print(list(filter(lambda i : i % 2 == 0,[1,2,3,4,5,6,7,8,9])))


# is_positive = lambda s: s < 0
# print(is_positive(-1))


# # 1;
# number = lambda s,d,f: s + d + f
# print(number(4,5,5))

# 2;
d = [1,2,4,5,7,7]
new = (lambda num: sum(num) / len(num))(d)
print(new)



# 3;
# new = lambda s: len(s) if len(s) > 5 else s
# print(new("pyt"))



# 4:


