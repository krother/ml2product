
# Docker

## Ziel

Die Datenquelle, die REST-API, die Datenbanken und überhaupt alles sollen als Docker-Container laufen.

## Schritt 1

Installiere Docker. Folge den Anweisungen auf der Docker Homepage.

## Schritte 2

Starte den Data Server über Docker.
Du benötigst das docker-compose.yml, requirements.txt und Dockerfile aus dem Repository:

    docker-compose build
    docker-compose up

## Schritt 3

Verändere docker-compose.yml und Dockerfile, um auch die Modell-API auf Docker zu starten.
