import pytest

from ukol_2 import secti


def test_secti_kladna_cisla():
    assert secti(2, 3) == 5


def test_secti_zaporne_cislo():
    assert secti(-1, 5) == 4


def test_secti_desetinna_cisla():
    assert secti(2.5, 1.5) == 4.0


def test_secti_neplatny_typ_a():
    with pytest.raises(TypeError):
        secti("2", 3)


def test_secti_neplatny_typ_b():
    with pytest.raises(TypeError):
        secti(2, None)
