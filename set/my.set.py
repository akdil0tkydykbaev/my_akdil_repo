# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
#
# people = ["Mike", "Bill", "Ted", "Bill"]
# print(people)
#
# users = set(people)
# print(users)
#
# users = set()
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# print(len(users))
#
# users = set()
# users.add("Sam")
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
# print(users)
#
# user = "Tom"
#
# if user in users:
#     users.remove(user)
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# users.discard("Tim")
# print(users)
#
# users.discard("Tom")  # элемент "Tom" есть, и метод удаляет элемент
# print(users)  # {"Bob", "Alice"}
#
# users.clear()
# print(users)
#
# users = {"Tom", "Bob", "Alice"}
#
# for user in users:
#     print(user)
#
# users = {"Tom", "Bob", "Alice"}
#
# students = users.copy()
# print(students)
#
# users = {"Tom", "Bob", "Alice"}
#
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.union(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# print(users | users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.intersection(users2)
# print(users3)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# print(users & users2)
#
# users = {"Tom", "Bob", "Alice", "Sam"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users2.intersection_update(users)
# print(users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.difference(users2)
# print(users3)
# print(users - users2)
#
# users = {"Tom", "Bob", "Alice"}
# users2 = {"Sam", "Kate", "Bob"}
#
# users3 = users.symmetric_difference(users2)
# print(users3)
#
# users4 = users ^ users2
# print(users4)
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issubset(superusers)) # True
#
# print(superusers.issubset(users)) # False
#
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
#
# print(users.issuperset(superusers)) # False
# print(superusers.issuperset(users)) # True
#
# #-----------------frozen set---------------
# users = {"Tom", "Bob", "Alice"}
#
# users = frozenset({"Tom", "Bob", "Alice"})
#
#
# students_python = {"Ainazik", "Ayana", "Akdil", "Fatima", "Zamirbek", "Mirbek", "Mederbek"}
# students_java = {"Azamat", "Kudaiberdi", "Zamirbek", "Mirbek", "Mederbek", "Talgarbek"}
#
# def student(students_python, students_java):
#
#     users3 = students_python.difference(students_java)
#     print(users3) #students_python
#
#     users4 = students_java.difference(students_python)
#     print(users4) # students_java
#
# a = student(students_python,students_java)



# students_python = {"Аяна", "Акдил", "Мирбек", "Талгарбек", "Бибигуль", "Замирбек"}
# students_java = {"Акдил", "Замирбек", "Кудайберди", "Медербек", "Айназик"}
#
# def stydent(students_java, students_python):
#     users3 = students_java.union(students_python)
#     print(users3)
#     users4 = students_java.intersection(students_python)
#     print(users4)
#
# a = stydent(students_python,students_java)



# students_python = {"Аяна", "Акдил", "Мирбек", "Талгарбек", "Бибигуль", "Замирбек"}
# students_java = {"Замирбек", "Кудайберди", "Медербек", "Айназик"}
#
# def student(students_java, students_python):
#     print(students_java & students_python)
#
#
# student(students_java,students_python)









# 1;
# sentence = "apple banana orange apple lemon banana"
#
# def work(sentenc):
#     w = set(sentenc.split())
#     a = sorted(w)
#     print(a)
#
# work(sentence)

# 2;
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# a = set(list1)
# b = set(list2)
# print(a & b)

# 3;
# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# print(set(numbers))

# 4;
# text = "hello world"
# a = set(text)
# print(a)
# -----------------------------------------------------FrozenSet--------------------------------------------------------
# 5;
# sers = frozenset({1,2,3,4,5})
# sers.add(2)
# print(sers)    # «frozenset» не имеет атрибута «добавить»

# 6;
# a = frozenset({1, 2, 3, 4, 5})
# b = frozenset({9, 5, 3, 1, 6})
#
# print(a & b)

# 7;
# z = frozenset({9, 5, 3, 1,3,3,4,4,2,4,6})

# user = 33
# if user in z:
#     z.remove(user)     # «frozenset» не имеет атрибута «удалить»
# print(z)

# 8;
# s = frozenset({1,2,2,2,3,3,4,5,5,6,7,8,8,9})
# a = s.difference() ------------------------------------------------
# print(a)


# a = (1,2,2,2,3,3,4,4,4,5,5,6,6,7,7,8,8,9)
# print(frozenset(a))