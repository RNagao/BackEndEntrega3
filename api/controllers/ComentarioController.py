from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.model.Comentario import Comentario
from api.serializers import ComentarioSerializer


class ComentarioList(APIView):
    def get(self, request):
        comentario = Comentario.objects.all()
        data = ComentarioSerializer(comentario, many=True).data
        return Response(data)

    def post(self, request):
        user = request.data['user']
        postagem = request.data['postagem']
        texto = request.data['comentario']
        comentario = Comentario(
            user= user,
            postagem= postagem,
            texto= texto
            )
        comentario.save()
        data = ComentarioSerializer(comentario).data
        return Response(data)