from .models import App
from rest_framework import serializers
from home.api.v1.serializers import UserSerializer
from .models import TYPE_CHOICES, FRAMEWORK_CHOICES


class AppSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    user = UserSerializer(read_only=True)
    description = serializers.CharField()
    type = serializers.ChoiceField(choices=TYPE_CHOICES, default=TYPE_CHOICES[0])
    framework = serializers.ChoiceField(choices=FRAMEWORK_CHOICES, default=FRAMEWORK_CHOICES[0])
    domain_name = serializers.CharField(max_length=50)
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = App
        fields = ['id', 'user', 'name', 'description', 'type', 'framework', 'domain_name', 'created_at', 'updated_at']
