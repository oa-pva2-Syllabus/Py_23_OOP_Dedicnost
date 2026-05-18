# test_streaming.py
import pytest
from streaming import Porad, Film, Serial


class TestPorad:
    def test_get_info(self):
        p = Porad("Inception", "Sci-fi")
        assert p.get_info() == "Název: Inception, Žánr: Sci-fi"


class TestFilm:
    def test_je_potomkem_porad(self):
        assert issubclass(Film, Porad)

    def test_get_info(self):
        f = Film("Inception", "Sci-fi", 148, 2010)
        assert f.get_info() == "Název: Inception, Žánr: Sci-fi, Délka: 148 min, Rok vydání: 2010"

    def test_celkova_delka(self):
        f = Film("Inception", "Sci-fi", 148, 2010)
        assert f.celkova_delka() == 148


class TestSerial:
    def test_je_potomkem_porad(self):
        assert issubclass(Serial, Porad)

    def test_get_info(self):
        s = Serial("Breaking Bad", "Drama", 62, 47)
        assert s.get_info() == "Název: Breaking Bad, Žánr: Drama, Počet epizod: 62, Délka epizody: 47 min"

    def test_celkova_delka(self):
        s = Serial("Breaking Bad", "Drama", 62, 47)
        assert s.celkova_delka() == 62 * 47


class TestDedicnost:
    def test_film_je_instance_porad(self):
        f = Film("Inception", "Sci-fi", 148, 2010)
        assert isinstance(f, Porad)

    def test_serial_je_instance_porad(self):
        s = Serial("Breaking Bad", "Drama", 62, 47)
        assert isinstance(s, Porad)

    def test_polymorfismus_get_info(self):
        porady = [
            Film("Inception", "Sci-fi", 148, 2010),
            Serial("Breaking Bad", "Drama", 62, 47),
        ]
        for porad in porady:
            assert isinstance(porad.get_info(), str)
            assert len(porad.get_info()) > 0
