from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.base, name='base'),
    path('view/', views.view, name='view'),
]