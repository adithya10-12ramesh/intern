# todo.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        return self.tasks

    def add_task(self, task):
        if not task.strip():
            raise ValueError("Task cannot be empty.")
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        raise IndexError("Task index out of range.")
