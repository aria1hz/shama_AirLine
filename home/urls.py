from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home, name='home'),
    path('tickets/',views.ticket, name='ticket'),
    path('loged/',views.loged, name='loged'),
]



