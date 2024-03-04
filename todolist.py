tasks = []

def add_task():
    task_description = input("Enter a new task: ")
    tasks.append({"description": task_description, "completed": False})
    print(f"New task '{task_description}' added successfully!\n")

def remove_task():
    show_tasks()
    if not tasks:
        return

    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['description']}' removed successfully!\n")
    else:
        print("Invalid task number. Please try again.\n")

def show_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"{index}. {task['description']} - {status}")
        print()

def complete_task():
    show_tasks()
    if not tasks:
        return

    task_number = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete!\n")
    else:
        print("Invalid task number. Please try again.\n")

def main():
    print("== Welcome to Your To-Do List ==")

    while True:
        print("1. Add a New Task")
        print("2. Remove a Task")
        print("3. Show Your Tasks")
        print("4. Mark Task as Complete")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
