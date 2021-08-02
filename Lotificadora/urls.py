"""Lotificadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.db.models import indexes
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app_lotificadora import views


urlpatterns = [
    #path('login/', views.login_view, name='login_view')
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('cliente/', views.cliente, name="cliente"),
    path('cliente/<int:id>/editar', views.mantenimiento_cliente, name="mantenimiento_cliente"),
    path('vendedor/', views.vendedor, name="vendedor"),
    path('contrato/', views.contrato, name="contrato"),
    path('terreno/', views.terreno, name="terreno"),
    path('pago/', views.pago, name="pago"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
