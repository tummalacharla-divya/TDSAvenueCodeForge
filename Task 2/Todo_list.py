""" Simple To-Do List
Build a program that allows users to add, 
remove, and view items on a to-do list."""
# Initialize an empty to-do list
to_do_list = []

# Function to display the to-do list
def view_tasks():
    if not to_do_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# Function to add a task
def add_task():
    task = input("\nEnter the task you want to add: ")
    to_do_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

# Function to remove a task
def remove_task():
    view_tasks()
    if to_do_list:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(to_do_list):
                removed_task = to_do_list.pop(task_num - 1)
                print(f"'{removed_task}' has been removed from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

# Function to display menu options
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

# Main program loop
if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("\nExiting the To-Do List program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
