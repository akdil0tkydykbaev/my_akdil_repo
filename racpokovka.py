# x, u = 1,2
# print(u)
# print(x)
#
# n = ["tom","bob","sam"]
# a,d,f = n
# print(a)
# print(d)
# print(f)
from tkinter.font import names

# x = {"arg": "hello","ard": "world","res": "3"}
# a,s,d = x
# print(a)
# print(s)
# print(d)
#
# print(x[s])


# p = ["tom","bob","daby"]
#
# for index,name in enumerate(p):
#     print(f"{index}.{name}")




# *d,k,l = [1,2,3,4,5]
#
# print(d)
# print(k)
# print(l)

# f,_,g,*_,k = [1,2,3,4,5,6,7,8]
#
# print(f)
# print(g)
# print(k)

# red, *other, green = {"red": "красный", "blue": "синий", "yellow": "желтый", "green": "зеленый"}
#
# print(red)
# print(green)
# print(other)

# nums1 = [1, 2, 3]
# nums2 = (4, 5, 6)
#
#
# nums3 = [*nums1, *nums2]
# print(nums3)

# dictionary1 = {"red": "красный", "blue": "синий"}
# dictionary2 = {"green": "зеленый", "yellow": "желтый"}
#
#
# dictionary3 = {**dictionary1, **dictionary2}
# print(dictionary3)

# n = [1,2,3]
# def sum(*args):
#     result = "0"
#     for arg in args:
#         result += arg
#     return result
#
#
# print(sum("1", "2",))  # 6
# print(sum(1, 2, 3, 4))  # 10
# print(sum(1, 2, 3, 4, 5))


# names = ["asta","tom","bob","sam" ]
# a,_,*s,_= names
# print(a)
# print(s)

# n = ("akdil")
# *_,g = n
# print(g)

# n1 = [1,2,3,4]
# n2 = [5,6,7,8]
#
# if  len(n1) == len(n2):
#     v = (*n1,*n2)
#     print(v)

# def sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
#
# print(sum(1, 2, 3))
# print(sum(1, 2, 3, 4))
# print(sum(1, 2, 3, 4, 5))

# 1:
a = 10
b = 20
print(b)
print(a)
# 2;
mixed_list = [1, "Hello", (10, 20), [30, 40]]
(a,s,d,f) = mixed_list
print(a)
print(s)
print(d)
print(f)
# 3:
def print_coordinates(a, s, d):
    print(f"a: {a}, s: {s}, d: {d}")

coordinates = [10, 20, 30]
print_coordinates(*coordinates)
# 4;
data = [[10, 20], [30, 40], [50, 60]]
a,s,d = data
print(a)
print(s)
print(d)
# 5:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a,s,d,*f,g,h = data
print(a)
print(s)
print(d)
print(f)
print(g)
print(h)
# 6;
data = [7, 14, 21, 28]
a, b, c, d = (n // 7 for n in data)

print(a, b, c, d)
# 7;
list1 = [100, 200]
list2 = [300, 400, 500, 600]
a1,*s1 = list1
a2,*s2 = list2
x = [a1,a2]
z = s1 + s2

print(x)
print(z)
























