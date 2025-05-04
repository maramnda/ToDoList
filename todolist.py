# This project:
# Input a task
# Delete a task
# View tasks
# Save the task to a file
# Exit project

todoFile = "tasks.txt"

# Load tasks from file
def loadTasks():
    try:
        with open(todoFile, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save task to file
def saveTasks(tasks):
    with open(todoFile, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

# Add new task
def newTask(tasks):
    task = input("Enter tasks: ").strip()
    if task:
        tasks.append(task)
        saveTasks(tasks)
        print(f"{task} has been added")
    else:
        print("You entered an empty task")

# Delete a task
def deleteTask(tasks):
    viewTask(tasks)
    if tasks:
        try:
            toDelete = int(input("Enter a task number to delete: "))
            if 1<= toDelete <= len(tasks):
                removed = tasks.pop(toDelete - 1)
                print(f"{removed} has been removed from your list")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")

# View tasks list
def viewTask(tasks):
    if not tasks:
        print("Your to do list is empty.")
    else:
        print("Your tasks")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main menu
def main():
    tasks = loadTasks()
    while True:
        print("")
        print("1. Enter task")
        print("2. Delete a task")
        print("3. View tasks")
        print("4. exit")
        print("")
        try:
            choice = int(input("Enter a number: "))
            if choice == 1:
                newTask(tasks)
            elif choice == 2:
                deleteTask(tasks)
            elif choice == 3:
                viewTask(tasks)
            elif choice == 4:
                print("GoodBye!")
                break
        except ValueError:
            print("Enter a valid number.")
        

if __name__ == "__main__":
    main()