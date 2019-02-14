"""frota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:


Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from frota.veiculos import views
from frota.core import views
from frota.veiculos import urls as veiculos_urls

urlpatterns = [
    url(r'^$',views.index),
    url(r'^veiculos/', include(veiculos_urls, namespace='veiculos')),
    url('admin/', admin.site.urls)]

if settings.DEBUG:
   urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

