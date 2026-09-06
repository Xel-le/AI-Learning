import pytest
from working import convert

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("dog")
    with pytest.raises(ValueError):
        convert("dog AM to cat PM")
    with pytest.raises(ValueError):
        convert("dogAMtocatPM")

def test_with_full_time():
    with pytest.raises(ValueError):
        convert("9:94 AM to 5:00 PM")
    assert convert("9:30 AM to 5:00 PM") == "09:30 to 17:00"
    assert convert("9:30AMto5:00PM") == "09:30 to 17:00"

def test_with_short_time():
    with pytest.raises(ValueError):
        convert("434 AM to 314324 PM")
    assert convert("10 AM to 6 PM") == "10:00 to 18:00"
    assert convert("10AMto6PM") == "10:00 to 18:00"

def test_with_mixed_time():
    with pytest.raises(ValueError):
        convert("9:94 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("32 AM to 5:00 PM")
    assert convert("7:30 AM to 8 PM") == "07:30 to 20:00"
    assert convert("7:30AMto8PM") == "07:30 to 20:00"

def test_midnight():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"
    assert convert("12:30 PM to 12:30 AM") == "12:30 to 00:30"
    