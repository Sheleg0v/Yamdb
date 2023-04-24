from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.shortcuts import get_object_or_404
from rest_framework import serializers, validators

from .models import User
from .validators import NotEqualValidator


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=settings.USER_CHAR_LENGTH,
        validators=[
            UnicodeUsernameValidator(),
            NotEqualValidator('me'),
        ],
        required=True)
    email = serializers.EmailField(max_length=254, required=True)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        model = User
        validators = [
            validators.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username', 'email')
            )
        ]


class MeSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        read_only_fields = ('role',)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=settings.USER_CHAR_LENGTH,
        validators=[
            UnicodeUsernameValidator(),
            NotEqualValidator('me'),
        ],
        required=True)
    confirmation_code = serializers.CharField(max_length=8)

    def validate(self, data):
        user = get_object_or_404(
            User,
            username=data['username']
        )
        if user.confirmation_code != data['confirmation_code'] or (
                user.confirmation_code == 0
        ):
            raise serializers.ValidationError('Неверный проверочный код!')
        return data
