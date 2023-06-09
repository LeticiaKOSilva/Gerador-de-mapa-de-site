from django.urls import path,include
from . import views
app_name = 'mapGenerator'

urlpatterns = [
    path('', views.index,name='index'),
    path('geradorDeMapaDeSite', views.index,name='index'),
    path('resultado?url=<str:url>', views.resultPage,name='result'),
    path('resultado?', views.resultPage,name='result'),

]