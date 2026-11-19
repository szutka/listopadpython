import pandas as pd
from dane import wczytaj_dane, wyswietl_dane

def test_wczytaj_dane_brak_plikow(tmp_path, monkeypatch):
    folder = tmp_path / "data"
    folder.mkdir()

    monkeypatch.chdir(tmp_path)

    wynik = wczytaj_dane()

    assert wynik is None

def test_wczytaj_dane_pliki(tmp_path, monkeypatch):
    folder = tmp_path / "data"
    folder.mkdir()

    plik = folder / "test.csv"
    plik.write_text(
        "miasto,temperatura\nGdansk,20\nKraków,25", encoding="utf-8"
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("builtins.input", lambda _: "1")

    wynik = wczytaj_dane()

    assert len(wynik) == 2