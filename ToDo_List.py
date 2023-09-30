class Task():
    def __init__(self, task_name, due_date, priority):
        self.task_name = task_name
        self.due_date = due_date
        self.priority = priority
    
    def __str__(self):
        return f"{self.task_name} (Due: {self.due_date}, Priority: {self.priority})"
    
class ToDoList():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task {task} added!")
    
    def remove_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                print(f"Task {task_name} removed!")
                return
        
        print(f"Task {task_name} not found!")

    def display_tasks(self):
        if not self.tasks:
            print("NO tasks available")
        else:
            print("Tasks available:")
            for task in self.tasks:
                print(task)

todo_list = ToDoList()

task1 = Task("Complete project", "2023-10-15", "High")
task2 = Task("Prepare presentation", "2023-10-20", "Medium")

todo_list.add_task(task1)
todo_list.add_task(task2)

todo_list.display_tasks()

todo_list.remove_task("Complete project")

todo_list.display_tasks()
