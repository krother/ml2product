
# MLFlow

## Ziel

Verwende MLFlow, um Deine Modelle zu verwalten.

## Schritt 1

Installiere [MLFlow](https://mlflow.org/)

    pip install mlflow

## Schritt 2 

Starte die MLFlow UI mit

    mlflow ui

Gehe im Browser auf [http://localhost:5000](http://localhost:5000).

## Schritt 3

Verändere Dein Skript zum Trainieren des Modells, so dass es MLFlow verwendet:

    import mlflow

Der Code zum Trainieren muß innerhalb eines **Context Managers** ausgeführt werden.
Füge den `with`-Block hinzu. Logge Hyperparameter, Metriken und das Modell:

    with mlflow.start_run():
        Xtrain, ytrain = my_preprocessing_function()
    
        trees = 77
        mlflow.log_param("n_estimators", trees)  # log a hyperparameters
        model = RandomForestClassifier(n_estimators=trees)  # or similar
        model.fit()

        acc = model.score(Xtrain, ytrain)
        model.log_metric("train_acc", acc)

        mlflow.sklearn.log_model(model, "model")

Das Modell kann ein `Pipeline`-Objekt sein, wenn Du auch die Präprozessoren speichern möchtest.

## Schritt 4

Führe das Modell Trainieren aus:

    python my_model.py

Es sollte ein Ordner `mlruns/` entstanden sein. 

## Schritt 5

Gehe auf das Dashboard und refreshe es.

Du solltest Dein Modell dort sehen.
Klicke auf den Eintrag, um zu sehen, was MLFlow gespeichert hat.

## Schritt 6

Starte eines der Modelle als API mit:

    mlflow models serve -p 1234 -m mlruns/0/69b0d6cfc5644c9c93ac2df377a3e5b9/artifacts/model/

Setze den Hash ein, den Du in der Übersicht des Modells siehst.
