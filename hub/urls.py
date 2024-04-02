from django.urls import path
from . import views

urlpatterns = [
    path('', views.hubs, name='hub'),
    path('<slug:slug>/', views.hub, name='hub'),
]