from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_poll, name='all_poll'),
    path('startapp/', views.starapp, name="start_app"),
    path('<int:tea_id>/', views.tea_detail, name="tea_details"),
    path('store/', views.tea_store_view, name="tea_store")
    
]