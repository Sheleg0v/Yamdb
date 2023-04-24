from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class GenreTitleInline(admin.TabularInline):
    model = Title.genre.through


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = ('name',)
    list_filter = ('id',)
    empty_value_display = '-пусто-'
    inlines = [GenreTitleInline]
    list_editable = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'title')
    search_fields = ('text', 'author', 'title')
    list_filter = ('text', 'author', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'review')
    search_fields = ('text', 'author', 'review')
    list_filter = ('text', 'author', 'review')


admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
