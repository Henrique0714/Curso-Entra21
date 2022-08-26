from django.shortcuts import render


# Create your views here.


def produtos(request):
    return render(request, 'produtos/produtos.html')


def teclados(request):
    return render(request, 'produtos/teclados.html')


def mouses(request):
    return render(request, 'produtos/mouses.html')


def headsets(request):
    return render(request, 'produtos/headsets.html')
