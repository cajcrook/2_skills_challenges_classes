import pytest
from lib.task_2 import TaskTracker

"""
Initial list is empty
"""
def test_initial_list_is_empty():
    tracker = TaskTracker()
    assert tracker.list_of_incomplete() == []

# """
# Add item to list
# Returns updated list
# """
def test_add_item_to_list():
    tracker = TaskTracker()
    tracker.add("Task_1")
    assert tracker.list_of_incomplete() == ["Task_1"]

"""
Add multiple items to list
Returns updated list showing multiple items
"""
def test_add_multiple_items_to_list():
    tracker = TaskTracker()
    tracker.add("Task_1")
    tracker.add("Task_2")
    tracker.add("Task_3")
    assert tracker.list_of_incomplete() == ["Task_1", "Task_2", "Task_3"]

"""
Add multiple items to list
Complete/ remove item from list
Returns updated list showing multiple items with removed item
"""
def test_add_multiple_items_mark_one_as_complete():
    tracker = TaskTracker()
    tracker.add("Task_1")
    tracker.add("Task_2")
    tracker.add("Task_3")
    tracker.add("Task_4")
    tracker.add("Task_5")
    tracker.completed_tasks(1)
    assert tracker.list_of_incomplete() == ["Task_1", "Task_3", "Task_4", "Task_5"]

"""
Add multiple items to list
Try to mark as complete a item that does not exist
Raising an error.
"""
def test_remove_incorrect_index():
    tracker = TaskTracker()
    tracker.add("Task_1")
    tracker.add("Task_2")
    tracker.add("Task_3")
    with pytest.raises(Exception) as err:
        tracker.completed_tasks(7) # raises an error "no such task to complete"
    assert str(err.value) == "no such task to complete"
    assert tracker.list_of_incomplete() == ["Task_1", "Task_2", "Task_3"]
