import pytest

from ukol_1 import pozdrav


def test_pozdrav_bezne_jmeno():
    assert pozdrav("Petra") == "Ahoj, Petra!"


def test_pozdrav_jine_jmeno():
    assert pozdrav("Jan") == "Ahoj, Jan!"


def test_pozdrav_prazdny_retezec():
    assert pozdrav("") == "Ahoj, !"


def test_pozdrav_neplatny_typ_int():
    with pytest.raises(TypeError):
        pozdrav(123)


def test_pozdrav_neplatny_typ_none():
    with pytest.raises(TypeError):
        pozdrav(None)
