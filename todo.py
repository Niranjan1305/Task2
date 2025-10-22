def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()


def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!\n")
    else:
        print("Task cannot be empty!\n")


def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed}' removed successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")


def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("To-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(filename, tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(filename, tasks)
        elif choice == "4":
            save_tasks(filename, tasks)
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice! Please select 1–4.\n")


if __name__ == "__main__":
    main()
