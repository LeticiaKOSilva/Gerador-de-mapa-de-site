from django.urls import path,include
from . import views
app_name = 'mapGenerator'

urlpatterns = [
    path('', views.index,name='index'),
    path('nomeDepoisDaBarra', views.pagina,name='pagina'),

]