from django.urls import path, include
from login import views

urlpatterns = [
    path('signup/', views.signup),
    path('', views.welcome)
]