from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.models import Fart, FartType
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, FartSerializer, TypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class FartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farts to be viewed or edited.
    """

    #queryset = Fart.objects.all()
    #serializer_class = FartSerializer
    def get_queryset(self):
            """
            Optionally restricts the returned purchases to a given user,
            by filtering against a `username` query parameter in the URL.
            """
            queryset = Fart.objects.all()
            username = self.request.query_params.get('username', None)
            if username is not None:
                queryset = queryset.filter(user.username=username)
            return queryset

class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farts to be viewed or edited.
    """

    queryset = FartType.objects.all()
    serializer_class = TypeSerializer
