from django.urls import path
from . import views

app_name = 'bime'

urlpatterns = [
    path('',views.bime, name='bime')
]
