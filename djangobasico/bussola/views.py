from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'bussola/bussola.html')

def norte(request):
    return render(request,'bussola/norte.html')