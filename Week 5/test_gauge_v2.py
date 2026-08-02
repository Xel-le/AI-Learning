import pytest
from gauge_v2 import convert
from gauge_v2 import gauge

def test_convert_zero_div():
    with pytest.raises(ValueError):
        convert("1/0")

def test_convert_not_string():
    with pytest.raises(ValueError):
        convert(1/1)

def test_not_string():
    with pytest.raises(ValueError):
        convert(1/1)

def test_convert_ok():
    assert convert("1/6") == 17


def test_gauge_str():
    with pytest.raises(ValueError):
        gauge("100")

def test_gauge_ok():
    assert gauge(17) == "17%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
