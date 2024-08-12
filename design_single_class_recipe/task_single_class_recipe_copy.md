# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

nouns = objects
add tasks, list of tasks tasks, complete tasks

verbs = functionality
list of tasks, remove completed tasks

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class TaskTracker():
    def add(self, task):
        parameter:
            string showing task

    def list_of_incomplete(self):
        returns:
            list [] of incomplete tasks 

    def completed_tasks(self, index):
        parameter:
            index to find position of task in list
        returns:
            updated list with task removed
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._
``` python
"""
Initial list is empty
"""
tracker = TaskTracker()
tracker.list_of_incomplete() => []

"""
Add item to list
Returns updated list
"""
tracker = TaskTracker()
tracker.add("Task_1")
tracker.list_of_incomplete() => ["Task_1"]

"""
Add multiple items to list
Returns updated list showing multiple items
"""
tracker = TaskTracker()
tracker.add("Task_1")
tracker.add("Task_2")
tracker.add("Task_3")
tracker.list_of_incomplete() => ["Task_1", "Task_2", "Task_3"]

"""
Add multiple items to list
Complete/ remove item from list
Returns updated list showing multiple items with removed item
"""
tracker = TaskTracker()
tracker.add("Task_1")
tracker.add("Task_2")
tracker.add("Task_3")
tracker.add("Task_4")
tracker.add("Task_5")
tracker.completed_tasks(1):
tracker.list_of_incomplete() => ["Task_1", "Task_2", "Task_3", "Task_4", "Task_5"]

"""
Add multiple items to list
Try to mark as complete a item that does not exist
Raising an error.
"""
tracker = TaskTracker()
tracker.add("Task_1")
tracker.add("Task_2")
tracker.add("Task_3")
tracker.completed_tasks(7) # raises an error "no such task to complete"
tracker.list_of_incomplete() => ["Task_1", "Task_2", "Task_3"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
