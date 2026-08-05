from rover_refactor import directions
import pytest


def test_turning():
    assert directions("r", [0, 0], 0) == ([0, 0], 1)
    assert directions("l", [0, 0], 0) == ([0, 0], 3)
    assert directions("ll", [0, 0], 0) == ([0, 0], 2)

def test_boundaries():
    assert directions("ffffffffffffffffffff", [0, 0], 0) == ([0, 10], 0)
    assert directions("bbbbbbbbbbbbbbbbbbbb", [0, 0], 0) == ([0, -10], 0)
    assert directions("lbbbbbbbbbbbbbbbbbbbb", [0, 0], 0) == ([10, 0], 3)
    assert directions("lffffffffffffffffffff", [0, 0], 0) == ([-10, 0], 3)

def test_continuity_and_mixed_commands():
    testing_position = [0, 0]
    testing_direction = 0
    assert directions("rffrbfflrffbrf", testing_position, testing_direction) == ([1, -2], 3)
    testing_position, testing_direction = directions("rffrbfflrffbrf", testing_position, testing_direction)
    assert directions("ff", testing_position, testing_direction) == ([-1, -2], 3)

