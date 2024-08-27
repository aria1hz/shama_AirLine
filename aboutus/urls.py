from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('',views.aboutus, name='aboutus')
]

