from django.urls import path
from crud import views

urlpatterns = [
    path('', views.home , name='home'),
    path('add/', views.add_emp , name='add_emp'),
    path('edit/<int:id>/', views.edit_emp, name='edit_emp'),
    path('delete/<int:id>/', views.delete_emp, name='delete_emp'),
]