from django.urls import path
from api.controllers.PostagemController import PostagemList
from api.controllers.ComentarioController import ComentarioList
from api.controllers.CompartilhamentoController import CompartilhamentoList
from api.controllers.CurtidaController import CurtidaList

from api.views import UserCreate, LoginView

urlpatterns = [
    path('postagem/', PostagemList.as_view()),
    path('comentario/', ComentarioList.as_view()),
    path('compartilhamento/', CompartilhamentoList.as_view()),
    path('curtida/', CurtidaList.as_view()),
    path('users/', UserCreate.as_view()),
    path('login/', LoginView.as_view())
]

