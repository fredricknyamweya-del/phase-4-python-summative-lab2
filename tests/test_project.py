import pytest
from models.user import User
from models.project import Project
from models.task import Task

def test_create_project():
    project = Project(1, "School Website", "Homepage build", "2026-06-30", [1])
    assert project.title == "School Website"
    assert project.users == [1]

def test_project_str():
    project = Project(2, "Library System", "CLI tool", "2026-07-15", [2])
    assert "Library System" in str(project)
