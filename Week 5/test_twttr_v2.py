import pytest
import twttr_v2

def test_vowels():
    for c in "aeuioy":
        assert twttr_v2.isVowel(c)

def test_not_vowels():
    for c in "qwrtpsdfghjklzxcvbnm":
        assert not twttr_v2.isVowel(c)

def test_numbers():
    for c in "1234567890":
        assert not twttr_v2.isVowel(c)

def test_shorten_all_vowels():
    with pytest.raises(SystemExit):
        twttr_v2.shorten("eyuioa")
    assert twttr_v2.shorten("eyu ioa") == " "

def test_shorten_no_vowels():
    assert twttr_v2.shorten("NVJGNXC<PGKCVN}xdfgvfgh") == "NVJGNXC<PGKCVN}xdfgvfgh"

def test_shorten_mix():
    assert twttr_v2.shorten("qwertyuiOpasdFGghjkl") == "qwrtpsdFGghjkl"