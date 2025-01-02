from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from notifications.models import Notification
from notifications.serializers import NotificationSerializer


class NotificationAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications.update(read=True)
        return Response({'detail': 'Notifications marked as read'}, status=200)
