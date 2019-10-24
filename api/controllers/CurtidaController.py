from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.model.Curtida import Curtida
from api.serializers import CurtidaSerializer


class CurtidaList(APIView):
    def get(self, request):
        postagem = Curtida.objects.all()
        data = CurtidaSerializer(postagem, many=True).data
        return Response(data)

    def post(self, request):
        texto = request.data['texto']
        numeroLikes = request.data['numeroLikes']
        numeroComentarios = request.data['numeroComentarios']
        numeroRts = request.data['numeroRts']
        postagem = Postagem(
            texto= texto,
            numeroLikes= numeroLikes,
            numeroComentarios= numeroComentarios,
            numeroRts= numeroRts 
            )
        postagem.save()
        data = PostagemSerializer(postagem).data
        return Response(data)