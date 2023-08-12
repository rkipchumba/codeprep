todo_list = []

# Display a menu with options for the user to interact with the to-do list. For example:


def display_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

# Allow the user to add tasks to the to-do list.


def add_task(task):
    todo_list.append(task)
    print('Task added succesfully')


def view_tasks():
    print("Tasks:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")


def mark_task_done(task_index):
    if 1 <= task_index <= len(todo_list):
        del todo_list[task_index - 1]
        print("Task marked as done and removed from the list.")


# Put it all together in a main loop.
while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        view_tasks()
        task_index = int(input("Enter the task number to mark as done: "))
        mark_task_done(task_index)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
