from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.model.Compartilhamento import Compartilhamento
from api.serializers import CompartilhamentoSerializer, UserSerializer


class CompartilhamentoList(APIView):
    def get(self, request):
        compartilhamento = Compartilhamento.objects.all()
        data = CompartilhamentoSerializer(compartilhamento, many=True).data
        return Response(data)

    def post(self, request):
        user = request.user
        postagem = request.data['postagem']
        compartilhamento = Compartilhamento(
            user= user,
            postagem= postagem,
            )
        compartilhamento.save()
        data = CompartilhamentoSerializer(compartilhamento).data
        return Response(data)