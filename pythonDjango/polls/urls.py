from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_poll, name='all_poll'),
    path('startapp/', views.starapp, name="start_app")
]