from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=70)
  roll = serializers.IntegerField()
  city = serializers.CharField(max_length=90)

  def create(self, validate_data):
    return User.objects.create(**validate_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.roll = validated_data.get('roll', instance.roll)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance
