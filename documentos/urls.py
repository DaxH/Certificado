from django.urls import path
from . import views

urlpatterns = [
        path('credenciales/', views.validar_credenciales, name = 'credenciales'),
        path('certificado/', views.mostrar_certificado, name = 'certificado'),
        path('certificado_create/', views.documento_create, name = 'certificado_create'),

]
