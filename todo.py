tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    if len(tasks) == 0:
        print("No tasks available to update.")
        return

    view_tasks()

    task_number = int(input("Enter the task number to update: "))

    if 1 <= task_number <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_number - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

while True:
    print("\n==============================")
    print("      TO-DO LIST MENU")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please enter a valid choice")