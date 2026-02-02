def load_tasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    clean_tasks = []
    for task in tasks:
        clean_tasks.append(task.strip())

    return clean_tasks


def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def show_menu(menu):
    print("\n=== Task Manager Menu ===")
    for index, item in enumerate(menu):
        print(index + 1, item)


def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for index, task in enumerate(tasks):
            print(index + 1, task)


def add_task(tasks):
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete")
        return

    for index, task in enumerate(tasks):
        print(index + 1, task)

    delete_choice = int(input("Enter task number to delete: "))

    if delete_choice < 1 or delete_choice > len(tasks):
        print("Invalid Choice")
    else:
        deleted_task = tasks.pop(delete_choice - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task}' deleted successfully!")


menu = ['View Task', 'Add Task', 'Delete Task', 'Exit']

while True:
    tasks = load_tasks()
    show_menu(menu)

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from the menu.")
        continue

    if choice < 1 or choice > len(menu):
        print("Invalid Choice")
        continue

    if choice == 4:
        print("Goodbye!")
        break

    if choice == 1:
        view_tasks(tasks)
    elif choice == 2:
        add_task(tasks)
    elif choice == 3:
        delete_task(tasks)
