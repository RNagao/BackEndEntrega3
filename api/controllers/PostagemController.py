from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.model.Postagem import Postagem
from api.serializers import PostagemSerializer

class PostagemList(APIView):
    def get(self, request):
        postagem = Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data

        return Response(data)

    def post(self, request):
        nome = request.data['nome']
        descricao = request.data['descricao']
        postagem = Postagem(nome= nome, descricao=descricao)
        postagem.save()
        data = PostagemSerializer(postagem).data

        return Response(data)