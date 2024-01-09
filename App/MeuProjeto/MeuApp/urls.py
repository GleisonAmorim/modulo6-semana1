from django.urls import path
from .views import InicioView, ContatoView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('contato/', ContatoView.as_view(), name='contato'),
]