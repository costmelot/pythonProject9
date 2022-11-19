import view
import modul as md

def run():
    while True:
        view.display_menu()

        choice = input("Выберите пункт меню: ")
        if choice == '1':
            md.add_student()
        elif choice == '2':
            md.view_students()
        elif choice == '3':
            md.search_student()
        elif choice == '4':
            md.update_student()
        elif choice == '5':
            md.delete_student()
        else:
            break

    print("-------------------------------")
    print(" Благодарим Вас за пользование нашей системой!")
    print("-------------------------------")



