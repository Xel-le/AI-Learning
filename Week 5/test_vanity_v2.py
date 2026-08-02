import pytest
from vanity_v2 import is_valid

#“All vanity plates must start with at least two letters.”
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”

def test_not_string():
    with pytest.raises(TypeError):
        is_valid(123456)

def test_not_two_letters_at_start():
    assert is_valid("123456") == False
    assert is_valid("C12345") == False

def test_longer_than_6_char():
    assert is_valid("AB34567") == False
    assert is_valid("AB34567547647325563462463636") == False

def test_less_than_2_char():
    assert is_valid("") == False
    assert is_valid("A") == False

def test_zero_first():
    assert is_valid("AB0457") == False

def test_num_in_middle():
    assert is_valid("AB145A") == False

def test_symbols():
    assert is_valid("AB 456") == False
    assert is_valid("AB_456") == False
    assert is_valid("AB/456") == False
    assert is_valid("AB.456") == False

def test_ok():
    assert is_valid("AB1234") == True
    assert is_valid("AB123") == True
    assert is_valid("AB") == True

