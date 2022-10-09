
# FastAPI

## Ziel

Das Modell ist über ein REST-API Interface benutzbar.

## Voraussetzung

Die Aufgabe **Refactoring** sollte vorher abgeschlossen sein.

## Schritt 1

* Schaut Euch den Code in `data_source/data_provider.py` an.
* Ihr findet die Dokumentation von FastAPI unter [fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

## Schritt 2

Erstellt einen API Endpoint `/model_version` das ein JSON-Dokument zurückgibt.
Darin sollten stehen:

* der Name des Modells
* eine Versionsnummer
* ein Zeitstempel mit dem Trainingszeitpunkt

Wenn Ihr erst ein Modell habt, könnt Ihr diese Informationen gerne direkt in das Python-Programm schreiben.
Später wird sich evtl. MLFlow darum kümmern.

## Schritt 3

Erstellt einen API Endpoint `/predict` das eine Vorhersage für einen Datenpunkt berechnet.

* Eingabeparameter ist ein JSON-Dokument mit sämtlichen Features.
* Ihr benötigt keine Parameterübergabe in der URL.
* Schickt die Features als **Request Body** (siehe [fastapi.tiangolo.com/tutorial/body/](https://fastapi.tiangolo.com/tutorial/body/))
* Verwendet zunächst eine GET Abfrage. Diese ist leichter zu debuggen.
* vergesst nicht, dass `model.predict()` ein DataFrame erwartet.

Schreibt ein JSON-Dokument als Beispiel-Eingabe.

## Schritt 4

* Startet den Server
* Geht auf `localhost:8000/docs`
* Probiert beide Endpoints aus.

## Schritt 5

* Fügt den neuen Code zum git-Repository hinzu

## Fragen

* wer sind mögliche Nutzer der API eines Modells?
* sollte das Trainieren des Modells über die API möglich sein?
* welche Anforderungen könnten entstehen, wenn die API von vielen Organisationen genutzt wird?
