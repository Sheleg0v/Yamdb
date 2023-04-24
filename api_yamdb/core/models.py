from django.conf import settings
from django.db import models
from users.models import User


class CommonCategoryGenre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=settings.CHAR_LENGTH
    )
    slug = models.SlugField(
        verbose_name='slug',
        unique=True,
        max_length=settings.SLUG_CHAR_LENGTH
    )

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name


class BaseReviewComment(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    class Meta:
        abstract = True
        ordering = ('pub_date',)
        verbose_name = None
        verbose_name_plural = None

    def __str__(self):
        return self.text[:15]
