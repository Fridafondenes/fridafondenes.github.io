
class ToDoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks, 1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{index}. {task.title} - {task.description} ({status})")


from to_do import ToDoItem, ToDoList

def main():
    my_todo_list = ToDoList()

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = ToDoItem(title, description)
            my_todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            print("\n===== Your Tasks =====")
            my_todo_list.view_tasks()

        elif choice == "3":
            my_todo_list.view_tasks()
            task_index = int(input("Enter the task number to mark as completed: ")) - 1

            try:
                task_to_complete = my_todo_list.tasks[task_index]
                task_to_complete.mark_as_completed()
                print(f"{task_to_complete.title} marked as completed!")
            except IndexError:
                print("Invalid task number. Please try again.")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
