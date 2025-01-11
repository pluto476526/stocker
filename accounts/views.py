# accounts/views.py

from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from accounts.permissions import IsSuperUserOnly
from accounts.serializers import RegisterSerializer, UserSerializer
from accounts.models import Profile

class RegisterView(APIView):
    """
    Allows users to register
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
    """
    Overides the post method to create a profile after registering the user
    """
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            Profile.objects.create(user=user)
            return Response({'detail': 'New user reqistered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthTokenView(ObtainAuthToken):
    """
    Assigns a unique authentication token
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username,
        })


class UserListViewSet(viewsets.ModelViewSet):
    """
    Allows superusers to view and edit users
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOnly]

    def create(self, request, *args, **kwargs):
    """
    Overides the create method
    Allows superusers to create users
    """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            Profile.objects.create(
                user = user,
                in_staff = True,
                in_superusers = True,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
