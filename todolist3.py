tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    elif choice == "3":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

        delete_num = int(input("Enter task number to delete: "))
        
        if 1 <= delete_num <= len(tasks):
            removed = tasks.pop(delete_num - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")