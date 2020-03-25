from django.urls import path
from . import views

urlpatterns = [
        path('credenciales/', views.validar_credenciales, name = 'credenciales'),
        path('certificado/', views.mostrar_certificado, name = 'certificado'),
        path('certificado_create/', views.documento_create, name = 'certificado_create'),
        path('certificado_list/', views.documento_list, name='certificado_list'),
        path('certificado_detail/<int:documento_pk>/', views.documento_detail, name='certificado_detail'),
        path('certificado_edit/<int:documento_pk>/', views.documento_edit, name='certificado_edit'),
        path('entidad_create/<int:documento_pk>/', views.entidad_create, name = 'entidad_create'),
        path('entidad_list/', views.entidad_list, name = 'entidad_list'),
        path('entidad_detail/<int:entidad_pk>/', views.entidad_detail, name = 'entidad_detail'),
        path('entidad_edit/<int:entidad_pk>/', views.entidad_edit, name = 'entidad_edit'),
]
