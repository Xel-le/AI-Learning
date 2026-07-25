import pytest
from twttr_v2 import shorten


def test_shorten_all_vowels():
    assert shorten("euioa") == ""
    assert shorten("eu ioa") == " "

def test_shorten_no_vowels():
    assert shorten("NVJGNXC<PGKCVN}xdfgvfgh") == "NVJGNXC<PGKCVN}xdfgvfgh"

def test_shorten_mix():
    assert shorten("qwertyuiOpasdFGghjkl") == "qwrtypsdFGghjkl"