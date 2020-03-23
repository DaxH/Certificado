from django.urls import path
from . import views

urlpatterns=[
        path('usuario_create/<int:documento_pk>/', views.usuario_create, name='usuario_create'),
        path('usuario_list/', views.usuario_list, name='usuario_list'),
        path('usuario_edit/<int:usuario_pk>/', views.usuario_edit, name='usuario_edit'),
        path('usuario_detail/<int:usuario_pk>/', views.usuario_detail, name='usuario_detail'),        

]
