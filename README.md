# YaMDb API

![example workflow](https://github.com/sheleg0v/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание проекта:

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

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Gaius-Capito/api_yamdb.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/source/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py makemigrations
```
```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```


Авторы: 
```
https://github.com/maxwellhousee - Максим Нуриев
```
```
https://github.com/Sheleg0v - Иван Шелегов
```
```
https://github.com/Gaius-Capito - Владислав Бунин
```