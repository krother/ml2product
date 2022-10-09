
# Datenquelle

## Ziel

Erhaltet Trainingsdaten über eine REST-API.

## Aufgabe

Die CSV-Datei, mit denen Ihr die Prototypen trainiert habt, werden wir in diesem Projekt nicht direkt verwenden.
In vielen Projekten erhaltet Ihr die Daten auf anderem Wege.
Hier verwenden wir eine REST-API.

## Schritt 1

Klone das Repository [github.com/krother/ml2product](github.com/krother/ml2product).
Du benötigst den gesamten Ordner `data_source/` .
Kopiere diesen Ordner in Dein Repository.

## Schritt 2

Kopiere die CSV-Datei `data_ex.csv` in den Ordner `data_source/` .

## Schritt 3

Installiere FastAPI:

    pip install fastapi uvicorn

## Schritt 4

Starte den Datenquell-Server mit:

    uvicorn rest_api:app --reload

## Schritt 5

Besuche die Seite der API

    http://localhost:8000/docs

Probiere die Endpoints direkt im Browser aus.

## Schritt 6

#### Hinweis

Über die REST-API erhaltet Ihr regelmäßig neue Daten.
Zu jeder vollen Stunde wird ein neues Datenpaket (*"chunk"*) freigeschaltet.


## Fragen

* was müßt Ihr tun, um die Datenquelle mit dem bestehenden Modell zu kombinieren?
* ist es grundsätzlich besser, mehr Daten zur Verfügung zu haben?
* wie solltest Du Modelle trainieren, wenn ständig neue Daten hinzu kommen?
* wie solltest Du Modelle testen und validieren, wenn ständig neue Daten hinzu kommen?
