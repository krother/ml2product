
# Monitoring

## Ziel

Beobachte Evaluationsmetriken über die Zeit.

## Schritt 1

* Trainiere ein Modell mit den ersten 10 chunks.
* Gleiche die **class imbalance** aus (z.B. mit `class_weights='balanced' in scikit)
* Speichere das Modell

## Schritt 2

Werte das Modell aus. Du kannst das gerne in einem Jupyter Notebook implementieren.

* Berechne Evaluationsmetriken (accuracy oder MSE) für jeden einzelnen chunk.
* Plotte die Metriken über die Zeit.
* wird das Modell besser oder schlechter?

## Hinweis

Um ein Dashboard mit Docker aufzusetzen, findest Du ein Tutorial auf [www.academis.eu/posts/data_analysis/pingubase/README.md](https://www.academis.eu/posts/data_analysis/pingubase/README.md) 


## Fragen

* Was ist **"model drift"**?
* Was sind die **"Lehmanns Laws"** of Software Engineering? Inwiefern gelten diese für Machine Learning Modelle?
