# accounts/urls.py

from rest_framework import routers
from django.urls import path, include
from accounts.views import (
    RegisterView,
    CustomObtainAuthTokenView,
    UserListViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserListViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', CustomObtainAuthTokenView.as_view()),
    path('', include(router.urls)),
]
