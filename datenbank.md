
# Datenbank

## Ziel

Es kann notwendig oder nützlich sein, eine Datenbank einzurichten.
Zum Beispiel um:

* Trainingsdaten aus der Datenquelle zu speichern
* Modelle für MLFlow zu speichern
* Evaluationsmetriken zu speichern

Entscheidet im Team, ob Ihr eine Datenbank einrichten möchtet, und wenn ja, welche.

**docker-compose** vereinfacht die Installation erheblich.

## PostGreSQL

Um einen Postgres-Server zu starten, erstelle eine Datei `docker-compose.yml`:

    version: '3'
    services:
    
      pg_database:
        image: postgres:13.0
        ports:
        - 5555:5432
        volumes:
        - ./sql_init/:/docker-entrypoint-initdb.d
        environment:
        - POSTGRES_PASSWORD=1234
        - POSTGRES_USER=postgres
        - POSTGRES_DB=mydbname

Erstelle einen Ordner `sql_init/` erstellen.
In diesem kannst Du SQL-Skripte ablegen, die beim **erstmaligen** erstellen des Containers ausgeführt werden.
Hier kannst Du z.B. `CREATE TABLE` Befehle hineinschreiben.

Starte den Container mit:

    docker compose up pg_database

#### Hinweis

Der Postgres-Server ist auf Port 5555 sichtbar, damit er nicht mit einer eventuell schon vorhandenen Installation kollidiert.


----

## MongoDB

Um einen MongoDB-Server zu starten, erstelle eine Datei `docker-compose.yml`
(oder erweitere eine Datei, die Du schon hast):

    version: '3'
    services:
    
      mongo_database:
        image: mongo
        ports:
        - 27017:27017

Starte den Container mit:

    docker compose up mongo_database
