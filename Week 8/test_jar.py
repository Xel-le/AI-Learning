from jar import Jar
import pytest

def test_initialize():
    blankJar = Jar(10)
    assert blankJar.capacity == 10
    assert str(blankJar) == ""
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")

def test_deposit():
    depositJar = Jar(10)
    depositJar.deposit(3)
    assert str(depositJar) == 3*"\U0001F36A"
    with pytest.raises(ValueError):
        depositJar.deposit(8)

def test_withdraw():
    withdrawJar = Jar(10)
    withdrawJar.deposit(3)
    assert str(withdrawJar) == 3*"\U0001F36A"
    withdrawJar.withdraw(2)
    assert str(withdrawJar) == 1*"\U0001F36A"
    withdrawJar.withdraw(1)
    assert str(withdrawJar) == ""
    with pytest.raises(ValueError):
        withdrawJar.withdraw(1)

