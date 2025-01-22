tasks = []  # A list to store tasks

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a Task")
    print("2. Show All Tasks")
    print("3. Delete a Task")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def show_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("\nEnter the task number to delete: "))
        removed_task = tasks.pop(task_no - 1)
        print(f"Task '{removed_task}' deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again!")

if __name__ == "__main__":
    main()
