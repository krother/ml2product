
# Docker

## Ziel

Die Datenquelle, die REST-API, die Datenbanken und überhaupt alles sollen als Docker-Container laufen.

## Schritt 1

Installiere Docker. Folge den Anweisungen auf der Docker Homepage.

## Schritt 2

Um einen einzelnen Container zu starten, schreibe im Verzeichnis mit dem Dockerfile:

    docker build -t my_container_name .
    docker run -d -p 8000:8000 my_container_name

Du kannst prüfen ob der Container läuft:

    docker ps

## Schritt 3

Starte den Data Server über Docker.
Du benötigst das docker-compose.yml, requirements.txt und Dockerfile aus dem Repository:

    docker-compose build
    docker-compose up

## Schritt 4

Verändere docker-compose.yml und Dockerfile, um auch die Modell-API auf Docker zu starten.

## Weitere Infos:

[Play with Docker Classroom](https://training.play-with-docker.com/)
