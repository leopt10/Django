from django.shortcuts import render

# Create your views here.


def paginaInicial(request):
    descricao = "DATA BINDING"
    numero = 4 + 6
    return render(request, "accounts/home.html", {"des": descricao, "num": numero})


def login(request):
    return render(request, "accounts/login.html")


def registro(request):
    return render(request, "accounts/registro.html")

