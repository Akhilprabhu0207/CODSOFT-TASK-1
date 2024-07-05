import os
def display_menu():
    print("To-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save and Quit")


def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt","r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks


def save_tasks(tasks):
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")


def add_task(tasks):
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    print("Task added.")


def mark_completed(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        print(f"Marked '{tasks[index]}' as completed.")
        tasks.pop(index)
    else:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        print(f"Deleted task: '{tasks[index]}'")
        tasks.pop(index)
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Your to-do list has been saved")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
