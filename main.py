from task_manager import *

while True:
    print("\n==== STUDENT TASK MANAGER ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        num = int(input("Enter task number: ")) - 1
        complete_task(num)

    elif choice == "4":
        view_tasks()
        num = int(input("Enter task number: ")) - 1
        delete_task(num)

    elif choice == "5":
        break

    else:
        print("Invalid choice")