from django.conf import settings
from django.core import validators
from django.db import models

from core.models import BaseReviewComment, CommonCategoryGenre
from .validator import year_validate


class Genre(CommonCategoryGenre):
    class Meta(CommonCategoryGenre.Meta):
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(CommonCategoryGenre):
    class Meta(CommonCategoryGenre.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Title(models.Model):
    name = models.CharField('Название', max_length=settings.CHAR_LENGTH)
    year = models.PositiveSmallIntegerField(
        'Год',
        db_index=True,
        validators=(year_validate,)
    )
    description = models.TextField('Описание', blank=True, null=True)
    genre = models.ManyToManyField(
        Genre,
        through='GenreTitle',
        blank=True,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        related_name='title',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)


class Review(BaseReviewComment):
    score = models.PositiveSmallIntegerField(
        'Оценка',
        default=7,
        validators=[
            validators.MinValueValidator(
                1,
                message='Минимальная оценка - 1'
            ),
            validators.MaxValueValidator(
                10,
                message='Максимальная оценка - 10'
            )
        ])
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )

    class Meta(BaseReviewComment.Meta):
        constraints = (
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_author_title_combination'
            ),
        )
        default_related_name = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comment(BaseReviewComment):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        verbose_name='Отзыв'
    )

    class Meta(BaseReviewComment.Meta):
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'
