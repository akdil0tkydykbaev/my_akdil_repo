# my_tuple = (1,"tom")
# print(my_tuple)
# from lib2to3.refactor import RefactoringTool


# name, age, company, position = ("Tom", 37, "Google", "software developer")
# print(name)         # Tom
# print(age)          # 37
# print(position)     # software developer
# print(company)
# tom = ("Tom", 37, "Google", "software developer")


# tom = ("Tom", 37, "Google", "software developer")
#
# # получем подкортеж с 1 по 3 элемента (не включая)
# print(tom[1:3])  # (37, "Google")
#
# # получем подкортеж с 0 по 3 элемента (не включая)
# print(tom[:3])  # ("Tom", 37, "Google")
#
# # получем подкортеж с 1 по послдений элемент
# print(tom[1:])  # (37, "Google", "software developer")




# n = (1,2,3,3,44,5,6,67,55)
# print(max(n))
# print(min(n))

# n = (1,2,3,3,44,5,6,67,55)
#
# max = n[0]
# min = n[0]
# for i in n:
#     if i < max:
#         max = i
#     if i > min:
#         min = i
#
# print(max)
# print(min)
#
# name = ("ASTA","ASCILAT","TORFIN","LECH")
# n = tuple(n for n in name if len(n) > 5)
# print(n)
#
#
#
#
# name = ("ASTA","ASCILAT","TORFIN","LECH",)
# n = tuple(i for i in name if i.startswith("A"))
# print(n)


# 1;
# numbers = (4, 7, 8, 2, 5, 8, 9, 8)
#
# n = numbers.index(8)
# print(n)

# 2;
# letters = ('a', 'b', 'c', 'a', 'd', 'a', 'e')
#
# count_1 = letters.count('a')
# print(count_1)

# 3;
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# a = tuple1
# z = tuple2
#
# print(a + z)

# 4;
# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)
# a = tuple1
# s = tuple2
# print(a == s)
# 5;
# string = "hello"
# print(tuple(string))
# 6;
# tuple1 = (1, 3, 5)
# tuple2 = (2, 4, 6)
# n = ()
# for i in range(len(tuple1)):
#     n += (tuple1[i],tuple2[i])
# print(n)
# -------------------------------------------------------------------------------------------------
"""
a1 = (1, 2, 3)
a2 = (4, 5, 6)
res = []
for i in range(len(a1)):
    res.append(a1[i] + a2[i])
    print(tuple(res))
a1 = (1, 2, 3)
a2 = (4, 5, 6)
res = []
for i in range(len(a1)):
    res.append(a1[i] + a2[i])
print(tuple(res))"""


# def num(tupie1,tuple2):
#     res = []
#     for i in range(len(tupie1)):
#         res.append(tupie1[i] + tuple2[i])
#         return tuple(res)
#
# tupie1 = (1,2,3)
# tuple2 = (4,5,6)
# res = num(tupie1,tuple2)
# print(res)


# def sum_tuples(t1, t2):
#     if len(t1) != len(t2):
#         return "Ошибка: кортежи должны быть одинаковой длины"
#
#     result = []
#     for i in range(len(t1)):
#         result.append(t1[i] + t2[i])
#
#     return tuple(result)
#
#
# result_sum = sum_tuples(tuple1, tuple2)
# print(result_sum)