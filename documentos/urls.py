from django.urls import path
from . import views

urlpatterns = [
        path(r'', views.validar_documento, name = 'documento'),
        path(r'certificado/', views.mostrar_certificado, name = 'certificado'),
]
