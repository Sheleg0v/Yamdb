from random import random

from django.conf import settings
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import (decorators, exceptions, filters, pagination,
                            permissions, status, viewsets)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .permissions import AdminOnly
from .serializers import (AuthSerializer, MeSerializer, TokenSerializer,
                          UserSerializer)


class UsersViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (AdminOnly,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

    @decorators.action(
        methods=['get', 'patch'],
        detail=False,
        permission_classes=(permissions.IsAuthenticated,),
    )
    def me(self, request, **kwargs):
        user = request.user
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)

        serializer = MeSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


@decorators.api_view(['POST'])
def token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    serializer.validate(serializer.data)
    refresh = RefreshToken.for_user(user)
    user.confirmation_code = 0
    user.save()
    return Response({'access': str(refresh.access_token)})


@decorators.api_view(['POST'])
def signup(request):
    confirmation_code = str(random())[2:8]
    serializer = AuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    current_email = serializer.validated_data['email']
    username = serializer.validated_data['username']
    error_message = 'Имя пользователя уже занято!!'
    try:
        user, created = User.objects.get_or_create(
            email=current_email,
            username=username,
        )
    except IntegrityError:
        if User.objects.filter(email=current_email).exists():
            error_message = 'Электронная почта уже занята!'
        raise exceptions.ValidationError(
            error_message,
            status.HTTP_400_BAD_REQUEST
        )

    send_mail(
        'Регистрация на портале YaMDB',
        f'Ваш проверочный код:{confirmation_code}',
        settings.EMAIL_ADDRESS,
        [current_email],
        fail_silently=False,
    )
    user.confirmation_code = confirmation_code
    user.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
