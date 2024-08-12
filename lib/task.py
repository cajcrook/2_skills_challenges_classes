
class TaskTracker():
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def incomplete_task_list(self):
        return self.tasks
    
    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise Exception("no such task to complete")
        del self.tasks[index]