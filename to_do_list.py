tasks = []
while True:
    print("\n--- TO-DO-LIST ---")
    print("1. Add Tasks.")
    print("2. View Tasks.")
    print("3. Remove Tasks.")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a task here: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour task:")
            for index in range(len(tasks)):
                print(index + 1, ".", tasks[index])

    elif choice == "3":
        if len(tasks) == 0:
            print("Empty. Nothing to remove here.")
        else:
            for index in range(len(tasks)):
                print(index + 1, ".", tasks[index])
            task_number = int(input("Enter the task number you want to remove: "))
            if task_number >= 1 and task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print("Removed:", removed_task)
            else:
                print("invalid task number")


    elif choice == "4":
        print("Goodbye!!!")
        break
    else:
        print("Invalid input. Enter a number between 1 and 4.")


'''
We started with printing the menu options/ choices for the user to choose from.
we then started work on each part.
'''
