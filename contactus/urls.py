from django.urls import path
from . import views

app_name = 'contactus'

urlpatterns = [
    path('', views.contactus, name='contactus'),
    path('success/', views.success, name='success'),
]