import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, details=""):
        task = {"id": len(self.tasks) + 1, "title": title, "details": details, "completed": False}
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{task['id']}. {task['title']} - {status}")

    def update_task(self, task_id, completed=False, details=""):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = completed
                task["details"] = details

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            self.tasks = json.load(file)

# Example Usage:
todo_app = ToDoList()
todo_app.add_task("Complete project")
todo_app.add_task("Go to the gym", "Do a 30-minute workout")
todo_app.display_tasks()

# Update task status
todo_app.update_task(1, completed=True)
todo_app.display_tasks()

# Save and load tasks
todo_app.save_to_file("todolist.json")
todo_app.load_from_file("todolist.json")
todo_app.display_tasks()
