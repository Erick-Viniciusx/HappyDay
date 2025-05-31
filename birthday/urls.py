from django.urls import path
from birthday import views

app_name = 'birthday'

urlpatterns = [
    path('dashboard/', views.index, name='dashboard'),
]