from django.shortcuts import render
from api.controllers.PostagemController import PostagemList
from api.controllers.ComentarioController import ComentarioList

from api.serializers import PostagemSerializer, ComentarioSerializer, CompartilhamentoSerializer, CurtidaSerializer, UserSerializer

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer