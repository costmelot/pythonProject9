import csv
from logger import LOG

student_fields = ['ID', 'Имя', 'Фамилия', 'факультет', 'курс']
student_database = 'students.csv'


@LOG
def add_student():
    print("-------------------------")
    print("Добавить новую запись.")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Введите " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Информация успешно сохранена.")
    input("Нажмите любую клавишу для продолжения.")
    return


def view_students():
    global student_fields
    global student_database

    print("--- Все записи ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Нажмите любую клавишу для продолжения.")


@LOG
def search_student():
    global student_fields
    global student_database

    print("--- Найти студента по ID ---")
    roll = input("Введите ID студента: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Запись найдена -----")
                    print("ID: ", row[0])
                    print("Имя: ", row[1])
                    print("Фамилия: ", row[2])
                    print("Факультет: ", row[3])
                    print("Курс: ", row[4])
                    break
        else:
            print("Такого ID нет в нашей базе")
    input("Нажмите любую клавишу для продолжения.")


@LOG
def update_student():
    global student_fields
    global student_database

    print("--- Обновить информацию о студенте ---")
    roll = input("Введите ID студента: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Запись найдена под номером: ", index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Введите " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Такого ID нет в нашей базе")

    input("Нажмите любую клавишу для продолжения.")


@LOG
def delete_student():
    global student_fields
    global student_database

    print("--- Удалить запись ---")
    roll = input("Введите ID студента: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Запись с ID", roll, "успешно удалена")
    else:
        print("Такого ID нет в нашей базе")

    input("Нажмите любую клавишу для продолжения.")
