from django.contrib.auth.models import User, Group
from cti.models import Apache_log

from django.core import exceptions
import django.contrib.auth.password_validation as validators


from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'last_login', 'first_name', 'last_name', 'is_staff', 'date_joined', 'password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 12}}

    def create(self, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "password" in validated_data:
            from django.contrib.auth.hashers import make_password
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)
    






class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']

class ApacheLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apache_log
        fields = ['id', 'url', 'log_file', 'created', 'analyzed']
