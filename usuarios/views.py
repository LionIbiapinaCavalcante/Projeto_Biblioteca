from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def login(request):
    if request.method == "GET":
        return render(request, 'login/login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        usuario = Usuario(email=email, password=password)
        usuario.save()
        return HttpResponse('Dados cadastrados com sucesso!')
