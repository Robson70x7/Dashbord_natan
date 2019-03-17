from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:client_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('edit/<int:client_id>/', views.edit, name='edit'),
    path('delete/<int:client_id>/', views.delete, name='delete'),
    path('create/save', views.saveclient, name='saveclient'),
]
