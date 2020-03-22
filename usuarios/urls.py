from django.urls import path
from . import views

urlpatterns=[
        path('usuario_create/<int:documento_pk>/', views.usuario_create, name='usuario_create'),
]
