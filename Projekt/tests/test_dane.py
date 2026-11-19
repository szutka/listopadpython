import pandas as pd
from dane import wczytaj_dane, wyswietl_dane

def test_wczytaj_dane_brak_plikow(tmp_path, monkeypatch):
    folder = tmp_path / "data"
    folder.mkdir()

    monkeypatch.chdir(tmp_path)

    wynik = wczytaj_dane()

    assert wynik is None