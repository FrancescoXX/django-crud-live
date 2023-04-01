from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('create', views.addUser),
    path('read/<str:pk>', views.getUser),
    path('update/<str:pk>', views.updateUser),
    path('delete/<str:pk>', views.deleteUser),
]