from task_manager import TaskManager
from database import Database


def print_menu():
    print("\nMenu:")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Wyświetl zadania według statusu")
    print("4. Edytuj zadanie")
    print("5. Usuń zadanie")
    print("6. Wyjście")


def get_task_details():
    title = input("Podaj tytuł zadania: ")
    description = input("Podaj opis zadania: ")
    return title, description


def print_task(task):
    print(task['title'] + ": " + task['description'] + ' | status: ' + task['status'])


def main():
    db = Database()
    manager = TaskManager(db)

    while True:
        print_menu()
        choice = input("Wybierz opcję: ")

        if choice == '1':
            title, description = get_task_details()
            task = manager.create_task(title, description)
            print(f"Utworzono zadanie: {task}")

        elif choice == '2':
            tasks = manager.list_tasks()
            for task in tasks:
                print_task(task)
            print()

        elif choice == '3':
            status = input("Podaj status (do zrobienia, w trakcie, zakończone): ")
            tasks = manager.list_tasks(status)
            for task in tasks:
                print_task(task)
            print()

        elif choice == '4':
            task_id = input("Podaj ID zadania do edycji: ")
            title = input("Podaj nowy tytuł (pozostaw puste, aby nie zmieniać): ")
            description = input("Podaj nowy opis (pozostaw puste, aby nie zmieniać): ")
            status = input("Podaj nowy status (do zrobienia, w trakcie, zakończone): ")
            if manager.update_task(task_id, title, description, status):
                print("Zadanie zaktualizowane.")
            else:
                print("Nie znaleziono zadania o podanym ID.")

        elif choice == '5':
            task_id = input("Podaj ID zadania do usunięcia: ")
            if manager.delete_task(task_id):
                print("Zadanie usunięte.")
            else:
                print("Nie znaleziono zadania o podanym ID.")

        elif choice == '6':
            print("Wyjście z aplikacji.")
            break

        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
