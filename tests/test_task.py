import pytest
from models.task import Task

def test_create_task():
    task = Task(1, "Design homepage", "Pending", 1, 1)
    assert task.status == "Pending"
    assert task.project == 1
    assert task.user == 1

def test_task_str():
    task = Task(2, "Write API", "In Progress", 1, 2)
    assert "Write API" in str(task)
