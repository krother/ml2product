
# Export aus Jupyter

## Ziel

Wandelt den Prototyp aus einem Jupyter Notebook in ein Python-Programm um.

## Schritt 1

* speichere das Notebook als `.py`-Datei (im Menü oben links)
* öffne die Datei in einem Editor (VSCode, PyCharm oder Spyder)

## Schritt 2

* lösche Leerzeilen
* lösche unnötige Kommentare (`In [1]:`)
* lösche unnötigen Code

## Schritt 3

* füge `print()` zu Zeilen hinzu, die etwas ausgeben sollen.
* sammle alle `import`-Anweisungen ganz oben.
* prüfe, dass das Programm noch läuft.

## Schritt 4

* entferne den EDA-Teil falls vorhanden (Plots und andere Voruntersuchungen).
* prüfe, dass das Programm noch läuft.

## Schritt 5

Verwende **black**, um den Code endgültig aufzuräumen:

    :::bash
    pip install black

    black myscript.py


## Schritt 6

* prüfe, dass das Programm noch läuft.
* füge das Programm dem gemeinsamen Repository hinzu
