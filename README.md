# python-flask-microservice
Python Flask Microservice API REST

## Running with Docker

Make sure you have Docker-compose.

```sh
$ docker-compose up -d
```

List containers.

```sh
$ docker ps
```

Create database in postgresql.

```sh
$ psql -h localhost -U postgres
$ create database flask;
```

Create schema in database flask.

```sh
$ docker exec -it flask_app_1 /bin/sh
$ EXPORT FLASK_APP=main
$ flask createdb
```

Restart app.

```sh
$ docker-compose down
$ docker-compose up -d
```

Acces to http://localhost/
