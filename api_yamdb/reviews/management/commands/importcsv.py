import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User


FILE_PATH: int = 0
MODEL_NAME: int = 1


class Command(BaseCommand):
    help = ('Добавляет данные в базу данных из csv файлов.'
            'Команда importcsv без аргументов или с аргументом all обновит все'
            'таблицы в БД.'
            'Команда importcsv с дополнительным аргументом <имя csv файла> '
            'обновит только таблицу, связанную с этим файлом.'
            'Пример: importcsv title обновит таблицу, '
            'связанную с моделью Title')
    _csv_files = {
        'users': (f'{settings.BASE_DIR}/static/data/users.csv', User),
        'genre': (f'{settings.BASE_DIR}/static/data/genre.csv', Genre),
        'category': (
            f'{settings.BASE_DIR}/static/data/category.csv',
            Category),
        'title': (f'{settings.BASE_DIR}/static/data/titles.csv', Title),
        'genre_title': (
            f'{settings.BASE_DIR}/static/data/genre_title.csv',
            GenreTitle),
        'review': (f'{settings.BASE_DIR}/static/data/review.csv', Review),
        'comments': (f'{settings.BASE_DIR}/static/data/comments.csv', Comment),
    }

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs='?', default='all')

    def handle(self, *args, **options):
        file_name = options['file_name']
        if file_name == 'all':
            for file_name in self._csv_files.keys():
                self.tables_csv_import(file_name)
        if file_name in ('category', 'genre'):
            self.category_genre_csv_import(file_name)
        self.tables_csv_import(file_name)

    def tables_csv_import(self, file_name):
        table_data = self._csv_files[file_name]
        with open(table_data[FILE_PATH], 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not table_data[MODEL_NAME].objects.filter(
                        pk=row['id']
                ).first():
                    row = {
                        key: int(value) if value.isdigit() else value
                        for key, value in row.items()
                    }
                    if row.get('category'):
                        row['category'] = Category.objects.get(
                            pk=row['category']
                        )
                    if row.get('author'):
                        row['author'] = User.objects.get(pk=row['author'])
                    table_data[MODEL_NAME].objects.create(**row)
                    self.stdout.write(
                        f'Обновление таблицы {table_data[MODEL_NAME]} '
                        f'успешно завершено'
                    )

    def category_genre_csv_import(self, file_name):
        table_data = self._csv_files[file_name]
        with open(table_data[FILE_PATH], 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not (table_data[MODEL_NAME].objects.filter(
                        pk=row['id']).first()
                        or table_data[MODEL_NAME].objects.filter(
                            slug=row['slug']).first()):
                    table_data[MODEL_NAME].objects.create(**row)
                    self.stdout.write(
                        f'Обновление таблицы {table_data[MODEL_NAME]} '
                        f'успешно завершено'
                    )
