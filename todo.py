# todo.py
from TodoList import TodoList
from datetime import datetime

def get_validated_task_number(todo_list):
    #Helper function to validate and return a task number from the user.
    try:
        task_number = int(input("Enter task number: "))
        if task_number <= 0 or task_number > todo_list.get_total_tasks():
            print("Invalid task number! Please enter a valid number.")
            return None
        return task_number
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None

def get_user_choice():
    #Helper function to get and validate user's menu choice.
    try:
        choice = int(input("\nEnter your choice (1-13): "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None
#This is my menu
def print_menu():
    #Prints the menu of options for the user.
    print("\nTo-Do List CLI App")
    print("1. Add task")
    print("2. List tasks ordered numerically")
    print("3. List tasks ordered alphabetically")
    print("4. Delete task")
    print("5. Add/Update a due date to a task")
    print("6. Add/Update a tag to a task")
    print("7. Delete all tasks")
    print("8. Edit task description")
    print("9. Show total number of tasks")
    print("10. Delete a due date to a task")
    print("11. Delegate task to someone else")
    print("12. Mark Task Complete")
    print("13. Quit")

def main():
    #Main function that runs the To-Do List CLI.
    todo_list = TodoList()

    while True:
        print_menu()
        choice = get_user_choice()
        if choice is None:
            continue  # Invalid input, prompt the menu again.

        if choice == 1: # 1. Add task
            task = input("Enter the task: ").strip()
            
            # Loops until correct choice is given
            while True:
                date_choice = input("Would you like to add a due date? (1: Yes, 2: No): ").strip()
                if date_choice in {'1', '2'}:
                    break
                print("Invalid input. Please enter '1' for Yes or '2' for No.")
            due_date = None
            if date_choice == '1':
                #Loops until date is in correct format
                while True:
                    due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
                    try:
                        #Checks if date is in correct format
                        datetime.strptime(due_date, "%Y-%m-%d")
                        break # Exits if format is correct
                    except ValueError:
                        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

            # Loops until proper priority is given
            while True:
                priority = input("Enter the priority (Low/Medium/High): ").strip().capitalize()
                if priority in {'Low', 'Medium', 'High'}:
                    break #Ends loop on correct answer
                print("Invalid priority. Please enter 'Low', 'Medium', or 'High'.")
            
            #Adds task to list
            todo_list.add_task(task, priority, due_date)

        elif choice == 2: # 2. List tasks ordered numerically
            todo_list.list_tasks_numeric()

        elif choice == 3: # 3. List tasks ordered alphabetically
            todo_list.list_tasks_alphabetic()

        elif choice == 4: # 4. Delete task
            task_number = get_validated_task_number(todo_list)
            if task_number:
                todo_list.delete_task(task_number)

        elif choice == 5: # 5. Add/Update a due date to a task
            task_number = get_validated_task_number(todo_list)
            if task_number:
                due_date = input("Enter a due date for the task (e.g., YYYY-MM-DD): ")
                todo_list.add_task_date(task_number, due_date)

        elif choice == 6: # 6. Add/Update a tag to a task
            task_number = get_validated_task_number(todo_list)
            if task_number:
                tag = input("Enter a tag for the task: ")
                todo_list.add_tag(task_number, tag)

        elif choice == 7: # 7. Delete all tasks
            todo_list.delete_all_tasks()

        elif choice == 8: # 8. Edit task description
            task_number = get_validated_task_number(todo_list)
            if task_number:
                desc = input("Enter new task description: ")
                todo_list.update_task(task_number, desc)

        elif choice == 9: # 9. Show total number of tasks
            total_tasks = todo_list.get_total_tasks()
            print(f'Total number of tasks: {total_tasks}')

        elif choice == 10: # 10. Delete a due date to a task
            task_number = get_validated_task_number(todo_list)
            if task_number:
                todo_list.remove_due_date(task_number)

        elif choice == 11: # 11. Delegate task to someone else
            task_number = get_validated_task_number(todo_list)
            if task_number:
                task_delegate = input("Enter the name of the delegate: ")
                todo_list.add_task_delegate(task_number, task_delegate)

        elif choice == 12: # 12. Mark Task Complete
            task_number = get_validated_task_number(todo_list)
            if task_number:
                todo_list.checkoff_task(task_number)

        elif choice == 13: # 13. Quit
            print("Exiting To-Do List CLI App. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == '__main__':
    main()
