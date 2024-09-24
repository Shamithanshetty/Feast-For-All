import matplotlib.pyplot as plt

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" deleted.')
        elif task in self.completed_tasks:
            self.completed_tasks.remove(task)
            print(f'Task "{task}" deleted from completed tasks.')
        else:
            print(f'Task "{task}" not found.')

    def mark_as_completed(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed_tasks.append(task)
            print(f'Task "{task}" marked as completed.')
        else:
            print(f'Task "{task}" not found in the to-do list.')

    def visualize_tasks(self):
        labels = ['To-Do', 'Completed']
        sizes = [len(self.tasks), len(self.completed_tasks)]
        colors = ['lightcoral', 'lightskyblue']
        explode = (0.1, 0)  # explode the 1st slice

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Task Distribution')
        plt.show()

def main():
    to_do_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Visualize Tasks (Pie Chart)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            to_do_list.add_task(task)

        elif choice == '2':
            task = input("Enter the task to delete: ")
            to_do_list.delete_task(task)

        elif choice == '3':
            task = input("Enter the task to mark as completed: ")
            to_do_list.mark_as_completed(task)

        elif choice == '4':
            to_do_list.visualize_tasks()

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
