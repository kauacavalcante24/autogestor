from django.contrib.auth import views
from django.urls import path

from .views import UserListView, UserRegisterView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='users'),
]
