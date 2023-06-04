from django.urls import path,include
from . import views
app_name = 'homePage'

urlpatterns = [
    path('', views.index,name='index'),
]