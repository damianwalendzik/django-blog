from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.CRUD_API_view, name='post-list'),
    path('<int:pk>/', views.CRUD_API_view, name='post-detail'),
    path('create/', views.CRUD_API_view, name='post-create'),
    path('<int:pk>/patch/', views.CRUD_API_view, name='post-patch'),
    path('<int:pk>/delete/', views.CRUD_API_view, name='post-delete'),
]