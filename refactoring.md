
# Refactoring

## Ziel

Strukturiert den vorhandenen Code neu.

## Schritt 1

Schreibt eine Funktion zum Trainieren des Modells.
Diese soll sich auch um die gesamte Präprozessierung kümmern.

Verwende die Signatur:

    def train(X: pd.DataFrame, y: pd.Series) -> sklearn.Estimator:
        """Preprocesses training data and trains a model."""
        ...

Fügt den neuen Code zum git-Repository hinzu.

## Schritt 2

Schreibt eine Funktion für die Inferenz mehrerer Datenpunkte.
Diese soll auch die Präprozessierung beinhalten.

Verwendet die Signatur:

    def predict(model: sklearn.Estimator, X: pd.DataFrame) -> Union[pd.Series, np.array]:
        """Returns a one-dimensional array or Series with predictions for multiple data points"""
        ...

Fügt den neuen Code zum git-Repository hinzu.

## Schritt 3

Schreibt eine Funktion für die Evaluierung eines Modells.
Diese soll auch die Präprozessierung beinhalten.

Verwendet die Signatur:

    def evaluate(model: sklearn.Estimator, X: pd.DataFrame, y: pd.Series) -> dict:
        """
        Evaluates a trained model on the given data.
        Returns a dictionary with multiple metrics.
        """
        ...

Fügt den neuen Code zum git-Repository hinzu.


## Schritt 4

Stellt sicher, dass das Programm immer noch funktioniert.

----

## Weiteres Material

Das Thema Refactoring geht noch viel, viel tiefer.
Für ausführlichere Refactorings sind unbedingt automatische Tests erforderlich.

* [Refactoring Tutorial von Kristian](https://www.academis.eu/posts/software_engineering/refactoring/README.md)
* [PyConDE 2022 Video](https://www.youtube.com/watch?v=13hVzP3Oofs)
* [Refactoring auf sourcemaking.com](https://sourcemaking.com/refactoring)
