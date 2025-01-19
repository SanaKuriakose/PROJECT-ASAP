#TO-DO LIST
def add_task(tasks):
    task = input("Enter a new task:")
    tasks.append({"task":task,"completed":False})
    print(f"Task'{task}'added!")
def view_tasks(tasks):
        for i,task in enumerate(tasks,start=1):
             if task['completed']:
                 status = "✔"
             else :
                status = "✘"
             print(f"{i}.{task['task']}[{status}]")
def mark_(tasks):
        view_tasks(tasks)
        try:
            task_num = int(input("Enter the task number to mark as completed:"))
            if 1<= task_num<=len(tasks):
                tasks[task_num-1]['completed'] = True
                print(f"Task'{tasks[task_num-1]['task']}'completed")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print(f"Task deleted..")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
def main():
    tasks = []
    print()
    print("To-Do List Menu:")
    print("1.Add Tasks")
    print("2.View Task")
    print("3.Mark Task as Completed")
    print("4.Delete tasks")
    print("5.Exit..\n")
    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_(tasks)
        elif choice =='4':
            delete_task(tasks)
        elif choice == "5":
            print("Exiting..")
            break
        else:
            print("Invalid choice. Please try again.")
main()