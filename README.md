# YaMDb API

![example workflow](https://github.com/sheleg0v/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

http://51.250.13.101/

## Описание проекта:

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения 
в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Взаимодействие с БД осуществляется через Api.

Стек:
- Django 3.2
- DRF 3.12.4
- djangorestframework-simplejwt 4.7.2
- PyJWT 2.1.0

Список запросов и эндпоинтов описан в документации ReDoc, доступной по адресу:

```
http://127.0.0.1:8000/redoc/
```

## Шаблон наполнения .env:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

## Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Sheleg0v/infra_sp2.git
```

Перейти в директорию infra:

```
cd infra_sp2/infra
```

Запустить docker-compose

```
docker-compose up -d --build
```

Выполнить миграции:

```
docker-compose exec web python manage.py makemigrations
```
```
docker-compose exec web python manage.py migrate
```

## Заполнение базы данных:
После запуска проекта выполните команду

```
docker-compose exec web python manage.py loaddata fixtures.json
```


### Авторы:
- https://github.com/maxwellhousee - Максим Нуриев
- https://github.com/Sheleg0v - Иван Шелегов
- https://github.com/Gaius-Capito - Владислав Бунин
