import pytest
from um import count

def test_mid():
    assert count("hi, um, hi") == 1
    assert count("hi, um, hi, um") == 2
    assert count("hi, um, hi, um?") == 2


def test_start():
    assert count("um") == 1
    assert count("um..") == 1
    assert count("um, hi") == 1

def test_mix():
    assert count("um,hi, um, hi, um") == 3
    assert count("       um  ,            hi, um, hi, um?") == 3

def test_none():
    assert count("umi") == 0
    assert count("yummy") == 0
    assert count("good umbrella") == 0
    assert count(" umbrella") == 0

def test_other():
    assert count("hi.um") == 1
    assert count("(um)") == 1