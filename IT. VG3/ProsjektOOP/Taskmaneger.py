class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = "Not Started"

    def mark_as_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.title} - {self.description} - Deadline: {self.deadline} - Status: {self.status}"


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Project: {self.name}\nTasks:\n{', '.join([str(task) for task in self.tasks])}"


class TaskManager:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def show_projects(self):
        for project in self.projects:
            print(project)


# Eksempel på bruk:
if __name__ == "__main__":
    task1 = Task("Implement Task Manager", "Create a simple Task Manager program", "2023-12-01")
    task2 = Task("Write Documentation", "Document the code and update README", "2023-12-05")

    project = Project("Task Manager Project")
    project.add_task(task1)
    project.add_task(task2)

    task_manager = TaskManager()
    task_manager.add_project(project)

    task_manager.show_projects()
