from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('role',)
    list_per_page = 20
    list_editable = ('role',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
