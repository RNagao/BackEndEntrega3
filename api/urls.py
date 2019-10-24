from django.urls import path
from api.controllers.PostagemController import PostagemList
from api.controllers.ComentarioController import ComentarioList

from api.views import UserCreate

urlpatterns = [
    path('postagem/', PostagemList.as_view()),
    path('comentario/', ComentarioList.as_view()),
    path('users/', UserCreate.as_view()),
]

