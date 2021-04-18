from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input', views.input, name='input'),
    path('export/csv/', views.export_users_csv, name='export_users_csv')
]