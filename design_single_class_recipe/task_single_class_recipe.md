# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class TaskTracker():
    def add(self, task):
        parameter:
            string representing a task.
    pass

    def incomplete_task_list(self):
        returns:
    def complete_task(self, index):
        parameter:
            index representing the postion of tast in list complete
        side effect:
            removes the task at index from the list        


## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._
``` python
"""
Initially there are no tasks.
"""
tracker = TaskTracker()
tracker.incomplete_task_list() => []

"""
When we add a task
It is shown in the list of taks
"""
tracker = TaskTracker()
tracker.add("Do the washing")
tracker.incomplete_task_list() => ["Do the washing"]

"""
When we add multiple task
They are shown in the list of taks
"""
tracker = TaskTracker()
tracker.add("Do the washing")
tracker.add("Make dinner")
tracker.add("Hoover")
tracker.incomplete_task_list() => ["Do the washing", "Make dinner", "Hoover"]

"""
When we add multiple task
And mark one as complete
It disappears from the list
"""
tracker = TaskTracker()
tracker.add("Do the washing")
tracker.add("Make dinner")
tracker.add("Hoover")
tracker.complete_task(1) 
tracker.incomplete_task_list() => ["Do the washing", "Hoover"]

"""
When we try to mark a task complete when it does not exist
It raises an error
"""
tracker = TaskTracker():
tracker.add("Do the washing")
tracker.complete_task(-1) # raises an error "no such task to complete (too low)"
tracker.incomplete_task_list() => ["Do the washing"]


"""
When we try to mark a task complete when it does not exist
It raises an error
"""
tracker = TaskTracker():
tracker.add("Do the washing")
tracker.complete_task(2)  # raises an error "no such task to complete(too high)"
tracker.incomplete_task_list() => ["Do the washing"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
