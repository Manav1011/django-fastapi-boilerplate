"""
URL configuration for django_fastapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from fastapi import APIRouter
from .views import root, healthcheck

# django urls
urlpatterns = [
    path('admin/', admin.site.urls)
]

base_router = APIRouter()

base_router.add_api_route("/", root, methods=["GET"], name="root")
base_router.add_api_route("/healthcheck", healthcheck, methods=["GET"], name="healthcheck")