
class TaskTracker():
    def __init__(self):
        self.tasks = []
    #   somewhere to store each task

    def add(self, task):
        self.tasks.append(task)
    # here this task is added (append) to the self.tasks above

    def list_of_incomplete(self):
        return self.tasks
    #     returns:
    #         list [] of incomplete tasks 
    # this returns a list of any incomplete task - returns the full list self.tasks

    def completed_tasks(self, index):
        if index < 0 or index >= len(self.tasks):
            raise Exception("no such task to complete")
        del self.tasks[index]
    #     parameter:
    #         index to find position of task in list
    #     returns:
    #         updated list with task removed
    #   this removes (del) a task from the self.tasks list if the index given is valid and applies to an item in the self.task list.
        