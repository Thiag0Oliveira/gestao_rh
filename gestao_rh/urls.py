
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionario/', include('apps.funcionario.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
