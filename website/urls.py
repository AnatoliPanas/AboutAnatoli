from django.urls import path
from . import views

# Указываем app_name для использования пространства имен в шаблонах (например, 'website:index')
app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-info/', views.get_info, name='get_info'),
]