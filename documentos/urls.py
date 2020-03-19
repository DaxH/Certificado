from django.urls import path
from . import views

urlpatterns = [
        path('credenciales/', views.validar_credenciales, name = 'credenciales'),
        path('certificado/', views.mostrar_certificado, name = 'certificado'),
        path('certificado_create/', views.documento_create, name = 'certificado_create'),
        path('certificado_list/', views.documento_list, name='certificado_list'),
]
