
# Monitoring

## Ziel

Beobachte Evaluationsmetriken über die Zeit.

## Schritt 1

* sammle Evaluationsmetriken für Trainings- und Testdaten für mehrere Modelle
* gib die Evaluationsmetriken aus

## Schritt 2

* evaluiere ein älteres Modell mit mehreren neueren Datensätzen (je ein *chunk*)
* plotte die Evaluationsmetriken über die Zeit.
* wird das Modell besser oder schlechter?

## Schritt 3

* berechne Modelle auf unterschiedlichen Versionen der Trainingsdaten (chunks 0-3, 0-4, 0-5 etc.)
* plotte die Evaluationsmetriken über die Zeit.
* wird das Modell besser oder schlechter?

## Hinweis

Du kannst Schritt 1-3 gerne in einem Jupyter Notebook durchführen.

Wenn Dir das zu einfach ist, kannst Du auch ein Dashboard aufsetzen.
Häufig verwendete Lösungen sind **Grafana**, **Kibana** und **Metabase**.

Du findest ein Tutorial um Metabase mit Docker aufzusetzen auf [www.academis.eu/posts/data_analysis/pingubase/README.md](https://www.academis.eu/posts/data_analysis/pingubase/README.md) 


## Fragen

* Was ist **"model drift"**?
* Was sind die **"Lehmanns Laws"** of Software Engineering? Inwiefern gelten diese für Machine Learning Modelle?
