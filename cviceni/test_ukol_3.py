import pytest

from ukol_3 import preved_na_text


def test_preved_na_text_cele_cislo():
    assert preved_na_text(5) == "Hodnota je 5"


def test_preved_na_text_desetinne_cislo():
    assert preved_na_text(3.14) == "Hodnota je 3.14"


def test_preved_na_text_nula():
    assert preved_na_text(0) == "Hodnota je 0"


def test_preved_na_text_neplatny_typ_str():
    with pytest.raises(TypeError):
        preved_na_text("5")


def test_preved_na_text_neplatny_typ_none():
    with pytest.raises(TypeError):
        preved_na_text(None)
