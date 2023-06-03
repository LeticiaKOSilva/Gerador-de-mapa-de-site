from django.shortcuts import render

def index(request):
    TEMPLATE_NAME = 'index.html'
    return render(request,TEMPLATE_NAME)

def pagina(request):
    TEMPLATE_NAME = 'mapGenerator/pagina2.html'
    return render(request,TEMPLATE_NAME)
