from bank_v2 import value
import pytest

def test_not_hello():
    assert value("123") == 100
    assert value("jedi") == 100
    assert value("bye") == 100

def test_h():
    assert value("hi") == 20
    assert value("hi there") == 20
    assert value("helo") == 20

def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0

def test_not_str():
    with pytest.raises(AttributeError):
        value(123)
    assert value("hello there") == 0
