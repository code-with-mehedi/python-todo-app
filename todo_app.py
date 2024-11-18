import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task+"\n")

def add_tasks(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("tasks added successfully")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        print("\n Your tasks")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")

def mark_task_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter valid task number")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no] += "-Done"
            save_tasks(tasks)
            print("Task marked as done")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Choose an option:")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("GoodBye")
            break
        else:
            print("Invalid option, please try again!")
        

if __name__ == "__main__":
    main()
