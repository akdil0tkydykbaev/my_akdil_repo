import random

students = ["Azamat", "Ainazik", "Ayana", "Nursultan", "Akdil", "Fatima", "Bibigul", "Kudaiberdi", "Zamirbek", "Mirbek", "Mederbek", "Talgarbek"]
def random_student():
    return random.choice(students)


def find_by_name_student():
    while True:
        print("У вас есть 5 попыток.")
        popitka = 5
        target_student = random_student()

        while popitka > 0:
            name = input("Введите имя студента: ")

            if name == target_student:
                print(f"{name} - это правильный ответ!")
                break
            else:
                popitka -= 1
                print(f"Вы не угадали. Попробуйте еще раз. У вас осталось {popitka} попыток.")
                if popitka < 3:
                    first_letter = target_student[0]
                    print(f"Подсказка: первая буква: {first_letter}")

        if popitka == 0:
            print(f"Попытки закончились. Загаданное имя было: {target_student}")

        answer = input("Желаете попробовать еще раз? (yes/no)\n")

        while answer != "yes" and answer != "no":
            answer = input("Некорректный ввод. Введите 'yes' или 'no':\n")

        if answer == "no":
            print(f"Спасибо за игру! Загаданное имя было: {target_student}")
            break


find_by_name_student()



print("\t\nakdil\n")
print("\tjgvukgu")