from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from api.model.Postagem import Postagem
from api.serializers import PostagemSerializer, UserSerializer


class PostagemList(APIView):
    def get(self, request):
        postagem = Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data
        return Response(data)

    def post(self, request):
        user = request.user
        texto = request.data['texto']
        numeroLikes = request.data['numeroLikes']
        numeroComentarios = request.data['numeroComentarios']
        numeroRts = request.data['numeroRts']
        postagem = Postagem(
            user= user.id,
            texto= texto,
            numeroLikes= numeroLikes,
            numeroComentarios= numeroComentarios,
            numeroRts= numeroRts 
            )
        postagem.save()
        data = PostagemSerializer(postagem).data
        return Response(data)