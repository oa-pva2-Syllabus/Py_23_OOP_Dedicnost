# test_uzivatel.py
import pytest
from streaming import Film, Serial, Uzivatel


class TestUzivatel:
    def test_pocatecni_stav(self):
        u = Uzivatel("jan123")
        assert u.get_sledovani() == "0 minut"

    def test_get_sledovani_minuty(self):
        u = Uzivatel("jan123")
        u.pridej_zhlednuti(45)
        assert u.get_sledovani() == "45 minut"

    def test_get_sledovani_hodiny_minuty(self):
        u = Uzivatel("jan123")
        u.pridej_zhlednuti(195)  # 3h 15min
        assert u.get_sledovani() == "3 hodin, 15 minut"

    def test_get_sledovani_dny_hodiny_minuty(self):
        u = Uzivatel("jan123")
        u.pridej_zhlednuti(2 * 24 * 60 + 3 * 60 + 15)
        assert u.get_sledovani() == "2 dní, 3 hodin, 15 minut"

    def test_pridej_zhlednuti_scitani(self):
        u = Uzivatel("jan123")
        u.pridej_zhlednuti(90)
        u.pridej_zhlednuti(90)
        assert u.get_sledovani() == "3 hodin, 0 minut"

    def test_pridej_zhlednuti_z_objektu(self):
        u = Uzivatel("jan123")
        f = Film("Inception", "Sci-fi", 148, 2010)
        s = Serial("Breaking Bad", "Drama", 2, 60)
        u.pridej_zhlednuti(f.celkova_delka())
        u.pridej_zhlednuti(s.celkova_delka())
        assert u.get_sledovani() == "4 hodin, 28 minut"
