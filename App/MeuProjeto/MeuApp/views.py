from django.shortcuts import render
from django.views import View

class InicioView(View):
    def get(self, request):
        return render(request, 'inicio.html')

class ContatoView(View):
    def get(self, request):
        return render(request, 'contato.html')