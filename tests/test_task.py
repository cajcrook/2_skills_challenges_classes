import pytest
from lib.task import TaskTracker

"""
Initially there are no tasks.
"""
def test_tracker_is_empty():    
    tracker = TaskTracker()
    assert tracker.incomplete_task_list() == []

"""
When we add a task
It is shown in the list of taks
"""
def test_add_item_to_task_tracker():
    tracker = TaskTracker()
    tracker.add("Do the washing")
    assert tracker.incomplete_task_list() == ["Do the washing"]

"""
When we add multiple task
They are shown in the list of taks
"""
def test_add_multiple_tasks_to_task_tracker():
    tracker = TaskTracker()
    tracker.add("Do the washing")
    tracker.add("Make dinner")
    tracker.add("Hoover")
    assert tracker.incomplete_task_list() == ["Do the washing", "Make dinner", "Hoover"]

"""
When we add multiple task
And mark one as complete
It disappears from the list
"""
def test_add_multiple_and_mark_one_completed_returns_updated_list():
    tracker = TaskTracker()
    tracker.add("Do the washing")
    tracker.add("Make dinner")
    tracker.add("Hoover")
    tracker.complete_task(1) 
    assert tracker.incomplete_task_list() == ["Do the washing", "Hoover"]

"""
When we try to mark a task complete when it does not exist
It raises an error
"""
def test_error_raises_when_index_too_low():
    tracker = TaskTracker()
    tracker.add("Do the washing")
    with pytest.raises(Exception) as err:
        tracker.complete_task(-1) # raises an error "no such task to complete (too low)"
    assert str(err.value) == "no such task to complete"
    assert tracker.incomplete_task_list() == ["Do the washing"]

"""
When we try to mark a task complete when it does not exist
It raises an error
"""
def test_error_raises_when_index_too_high():
    tracker = TaskTracker()
    tracker.add("Do the washing")
    with pytest.raises(Exception) as err:
        tracker.complete_task(1)  # raises an error "no such task to complete(too high)"
    assert str(err.value) == "no such task to complete"
    assert tracker.incomplete_task_list() == ["Do the washing"]
