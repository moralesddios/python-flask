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

Test postgresql connection (password=secret).

```sh
$ psql -h localhost -U postgres
$ \l;
```

Create schema in database flask.

```sh
$ docker exec -it flask_app_1 bash
$ export FLASK_APP=main
$ flask createdb
```

Restart app.

```sh
$ docker-compose down
$ docker-compose up -d
```


Your app should now be running on localhost:80.
