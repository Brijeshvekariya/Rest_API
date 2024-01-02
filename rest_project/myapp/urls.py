from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('api/book',views.booklistview),
    path('api/book/<int:pk>',views.bookDetailView),
]