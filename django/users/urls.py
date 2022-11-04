from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
]
