from rest_framework import serializers
from .models import Factory, Machine


class FactorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Factory
        fields = ("id", "user", "user_id", "city", "daily_production", "name")


class MachineSerializer(serializers.ModelSerializer):
    factory = serializers.StringRelatedField()
    factory_id = serializers.IntegerField(required=True)

    class Meta:
        model = Machine
        fields = ("id", "factory", "factory_id",
                  "power", "name")
