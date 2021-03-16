from django.contrib.auth.models import User, Group
from cti.models import Apache_log


from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']

class ApacheLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apache_log
        fields = ['id', 'url', 'log_file', 'created', 'analyzed']
