tasks=[]

def add_task(task):
    tasks.append(task)
    print(f"The new tasks list is: {tasks}.")

def remove_task(i):
    try:
        removed_task=tasks.pop(i-1)
        print(f"Task number {i} will be removed from the list.")
        print(f"New tasks list is: {tasks}")
    except:
        print(f"There is no task with index number {i}")


def save_tasks():
    with open('tasks.txt','w') as task_file:
        for t in tasks:
            task_file.write(f"{t}\n")
        print("Tasks saved in file!")

def read_tasks_in_file():
    print("Your tasks are as follows: ")
    with open('tasks.txt','rt') as file:
        content=file.read()
        for line in content.split():
            print(line)
    print("DO REMEMBER TO COMPLETE THEM!!")

def show_list(tasks):
    print("The tasks that you have to complete are: ", tasks)

while True:
    print("\nEnter 1 to add tasks")
    print("\nEnter 2 to remove tasks")
    print("\nEnter 3 to save tasks.")
    print("\nEnter 4 to read tasks from file.")
    print("\nEnter 5 to see the final list on console.")
    
    try:
        choice=int(input("Enter your choice: "))
    
        if choice == 1:
            task=input("Enter which task you want to add: ")
            add_task(task)
    
        elif choice == 2:
            i=int(input("Enter the index number of the task that you want to remove: "))
            remove_task(i)
    
        elif choice == 3:
            save_tasks()
    
        elif choice == 4:
            read_tasks_in_file()

        elif choice == 5:
            show_list(tasks)
            
        else:
            print("Invalid choice!")
    
    except:
        print("Enter only numbers!")

