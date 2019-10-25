from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.model.Curtida import Curtida
from api.serializers import CurtidaSerializer, UserSerializer


class CurtidaList(APIView):
    def get(self, request):
        curtida = Curtida.objects.all()
        data = CurtidaSerializer(curtida, many=True).data
        return Response(data)

    def post(self, request):
        user = request.user
        postagem = request.data['postagem']
        curtida = Curtida(
            user= user,
            postagem= postagem,
            )
        curtida.save()
        data = CurtidaSerializer(curtida).data
        return Response(data)