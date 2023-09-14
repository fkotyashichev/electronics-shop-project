from src.keyboard import Keyboard
import pytest


@pytest.fixture()
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_magic(kb):
    assert str(kb) == "Dark Project KD87A"

def test_language(kb):
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"

    with pytest.raises(AttributeError)
        kb.language = 'CH'
