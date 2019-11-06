from django.contrib.auth.models import User, Group
from api.models import Fart, Type
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class FartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fart
        fields = ['user', 'score', 'type', 'smell_scale', 'noise_scale', 'city', 'date_farted']
        depth = 1


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['name']
