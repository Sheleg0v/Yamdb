from django.urls import include, path
from rest_framework import routers

from .views import signup, token, UsersViewSet


router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', signup),
    path('auth/token/', token),
]
