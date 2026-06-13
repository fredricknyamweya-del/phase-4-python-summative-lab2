import pytest
from models.user import User

def test_create_user():
    user = User(1, "Alice", "alice@example.com")
    assert user.id == 1
    assert user.name == "Alice"
    assert user.email == "alice@example.com"

def test_user_str():
    user = User(2, "Bob", "bob@example.com")
    assert str(user) == "User(id=2, name=Bob, email=bob@example.com)"
