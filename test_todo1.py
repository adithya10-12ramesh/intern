# test_todo.py

import pytest
from todo import TodoList

def test_add_task():
    todo = TodoList()
    todo.add_task("Buy milk")
    assert todo.view_tasks() == ["Buy milk"]

def test_add_empty_task_raises():
    todo = TodoList()
    with pytest.raises(ValueError):
        todo.add_task("   ")

def test_view_tasks_empty():
    todo = TodoList()
    assert todo.view_tasks() == []

def test_remove_task():
    todo = TodoList()
    todo.add_task("Task 1")
    todo.add_task("Task 2")
    removed = todo.remove_task(0)
    assert removed == "Task 1"
    assert todo.view_tasks() == ["Task 2"]

def test_remove_invalid_index():
    todo = TodoList()
    todo.add_task("Task 1")
    with pytest.raises(IndexError):
        todo.remove_task(5)
