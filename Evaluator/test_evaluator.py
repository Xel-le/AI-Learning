import pytest
from evaluator import calculate

def test_initial():
    assert calculate("3 + 4") == 7.0
    assert calculate("3 + 4 * 2") == 11.0
    assert calculate("3 * 4 + 2") == 14.0
    assert calculate("10 - 2 - 3") == 5.0
    assert calculate("8 / 2 / 2") == 2.0
    assert calculate("2 + 3 * 4 - 1") == 13.0

def test_precedence():
    assert calculate("2 + 3 * 4") == 14.0
    assert calculate("2 * 3 + 4") == 10.0
    assert calculate("2 + 3 * 4 + 5") == 19.0
    assert calculate("100 - 10 * 2") == 80.0
    assert calculate("2 * 3 + 4 * 5") == 26.0 

def test_associativity():
    assert calculate("10 - 2 - 3") == 5.0  
    assert calculate("20 / 2 / 5") == 2.0   
    assert calculate("10 - 5 + 3") == 8.0       
    assert calculate("2 - 3 + 4 - 5") == -2.0     
    assert calculate("100 / 10 / 2 * 5") == 25.0