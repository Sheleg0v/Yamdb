# YaMDb API

## Project description:

The YaMDb project collects user reviews of works. The works themselves 
are not stored in YaMDb, you cannot watch a movie or listen to music here.

Interaction with the database is carried out through the Api.

Stack:
- Django 3.2
- DRF 3.12.4
- djangorestframework-simplejwt 4.7.2
- PyJWT 2.1.0
- gunicorn 20.0.4
- nginx
- PostgreSQL

The list of requests and endpoints is described in the ReDoc documentation, available at:

```
http://127.0.0.1:8000/redoc/
```

## Filling template .env:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

## Project launch:
Clone the repository:

```
git clone git@github.com:Sheleg0v/yamdb_final
```

Change directory on the command line:

```
cd amdb_final/infra
```

launch docker-compose

```
docker-compose up -d --build
```

Apply migrations:

```
docker-compose exec web python manage.py makemigrations
```
```
docker-compose exec web python manage.py migrate
```

## Filling in the database:
After launching project run this command:

```
docker-compose exec web python manage.py loaddata fixtures.json
```


### Author:
- https://github.com/Sheleg0v - Иван Шелегов
