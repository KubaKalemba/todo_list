from task_manager import TaskManager
from database import Database


def print_menu():
    print("\nMenu:")
    print("1 -> Add task ")
    print("2 -> Display tasks")
    print("3 -> Display tasks based on status (to do; done; in progress")
    print("4 -> Edit task")
    print("5 -> Delete tasl")
    print("0 -> Exit")


def get_task_details():
    title = input("Write task title ")
    description = input("Write task description ")
    return title, description


def print_task(task):
    print(task['title'] + ": " + task['description'] + ' | status: ' + task['status'])


def main():
    db = Database()
    manager = TaskManager(db)

    while True:
        print_menu()
        choice = input("Choose option! ")

        if choice == '1':
            title, description = get_task_details()
            task = manager.create_task(title, description)
            print(f"Task created: {task}")

        elif choice == '2':
            tasks = manager.list_tasks()
            for task in tasks:
                print_task(task)
            print()

        elif choice == '3':
            status = input("Give new status. 1 -> to do ; 2 -> done ; 3 -> in progress")
            if status == 1:
                status = "to do"
            elif status == 2:
                status = "done"
            elif status == 3:
                status = "in progress"
            else:
                status = "to do"

            tasks = manager.list_tasks(status)
            for task in tasks:
                print_task(task)
            print()

        elif choice == '4':
            task_id = input("Give ID of the task")
            title = input("New title (leave empty if you dont want to change it)")
            description = input("New description (leave empty if you dont want to change it)")

            status = input("Give new status. 1 -> to do ; 2 -> done ; 3 -> in progress")
            if status == 1:
                status = "to do"
            elif status == 2:
                status = "done"
            elif status == 3:
                status = "in progress"
            else:
                status = None

            if manager.update_task(task_id, title, description, status):
                print("Task updated!")
            else:
                print("Task with id" + task_id + " not found!")

        elif choice == '5':
            task_id = input("Give ID of the task")
            if manager.delete_task(task_id):
                print("Task deleted!")
            else:
                print("Task with id" + task_id + " not found!")

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Wrong input!")


if __name__ == "__main__":
    main()
