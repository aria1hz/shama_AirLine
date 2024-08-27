from django.urls import path
from . import views

app_name = 'viza'

urlpatterns = [
    path('',views.viza, name='viza'),
    path('single_viza',views.single_viza, name='single_viza'),
    path('<slug:slug>',views.single_viza, name='single_viza'),
]

