from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from notifications.models import Notification
from notifications.serializers import NotificationSerializer


class NotificationAPIView(APIView):
    """
    Allows warehouse managers to view noifications on products with low stock counts
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Dispalys unread notifications
        """
        notifications = Notification.objects.filter(recipient=request.user, read=False).order_by('-timestamp')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        """
        Marks all unread notifications as read
        """
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        notifications.update(read=True)
        return Response({'detail': 'Notifications marked as read'}, status=200)
