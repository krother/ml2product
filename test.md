
# Automatische Tests

## Ziel

Die API Endpoints werden automatisch getestet.

## Schritt 1

* Bearbeitet das erste Kapitel in [Kristians Pytest Tutorial](https://www.academis.eu/python_testing)

## Schritt 2

* erstellt einen Test Client entsprechend der [FastAPI Dokumentation](https://fastapi.tiangolo.com/tutorial/testing/)
* schreibt einen Test für den Endpoint `predict()`
* führt den Test mit `pytest` aus

## Schritt 3

Schreibt den Test so, dass er nicht gleich scheitert, wenn Ihr das Modell neu trainiert.
Also nicht:

    assert probability = 0.1234567

Sondern:

    assert 0.0 <= probability <= 1.0

**Die Aufgabe des Tests ist sicherzustellen, dass das Programm technisch funktioniert, nicht dass das Modell gut ist.**

## Schritt 4

* Ihr könnt die übrigen API Endpoints unter Euch aufteilen.

## Schritt 5

Sichere die Änderungen am Code auf git.
