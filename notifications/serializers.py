from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target = serializers.CharField(source='target.__str__', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target', 'timestamp', 'read']
