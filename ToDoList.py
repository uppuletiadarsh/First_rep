import json

tasks = []

def display_menu():
    print("Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Save tasks to file")
    print("5. Load tasks from file")
    print("6. Exit")

def view_tasks():
    print("Current Tasks:")
    if not tasks:
        print("No tasks.")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task_name']} - Due: {task['due_date']} - Priority: {task['priority']}")
    print()

def add_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append({"task_name": task_name, "due_date": due_date, "priority": priority})
    print("Task added.\n")

def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter index of task to remove: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task removed.\n")
            else:
                print("Invalid index.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    else:
        print("No tasks to remove.\n")

def save_tasks_to_file():
    if tasks:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Tasks saved to file.\n")
    else:
        print("No tasks to save.\n")

def load_tasks_from_file():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded from file.\n")
    except FileNotFoundError:
        print("File not found.\n")
    except json.JSONDecodeError:
        print("Invalid JSON format in file.\n")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        save_tasks_to_file()
    elif choice == '5':
        load_tasks_from_file()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
