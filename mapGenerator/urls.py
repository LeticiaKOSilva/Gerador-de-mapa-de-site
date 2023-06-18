from django.urls import path
from . import views

app_name = 'mapGenerator'

urlpatterns = [
    path('', views.index, name='index'),
    path('geradorDeMapaDeSite', views.index, name='index'),
    path('resultado?url=<str:url>', views.result, name='result'),
    path('resultado/', views.result, name='result'),
    path('download-xml?url=<str:url>', views.download_xml, name='download-xml'),
    path('download-xml/', views.download_xml, name='download-xml'),
    path('occurrence?url=<str:url>', views.occurrence, name='occurrence'),
    path('occurrence/', views.occurrence, name='occurrence'),
]