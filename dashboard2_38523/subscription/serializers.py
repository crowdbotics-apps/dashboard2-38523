from .models import App
from .models import Subscription
from rest_framework import serializers
from ..app.serializers import AppSerializer
from ..plan.serializers import PlanSerializer
from home.api.v1.serializers import UserSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    active = serializers.BooleanField()
    user = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'plan', 'app', 'active', 'created_at', 'updated_at']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["plan"] = PlanSerializer(instance.plan).data
        data["app"] = AppSerializer(instance.app).data
        return data
