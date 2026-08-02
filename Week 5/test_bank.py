from bank_v2 import value
import pytest

def test_not_hello():
    assert value("123") == 100
    assert value("jedi") == 100
    assert value("Bye") == 100

def test_h():
    assert value("hI") == 20
    assert value("hi thEre") == 20
    assert value("Helo") == 20

def test_hello():
    assert value("hEllo") == 0
    assert value("Hello there") == 0

def test_not_str():
    with pytest.raises(AttributeError):
        value(123)
    assert value("hello there") == 0
