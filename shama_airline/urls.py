"""
URL configuration for shama_airline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('account/',include('account.urls')),
    path('contactus/',include('contactus.urls')),
    path('viza/',include('viza.urls')),
    path('bime/',include('bime.urls')),
    path('aboutus/',include('aboutus.urls')),
    # path('tickets/',include('tickets.urls')),
    # static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT) 
