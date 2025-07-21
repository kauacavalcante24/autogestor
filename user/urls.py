from django.urls import path
from django.contrib.auth import views
from .views import UserRegisterView, UserListView


urlpatterns = [
    path('user/login', views.LoginView.as_view(), name='login'),
    path('user/register', UserRegisterView.as_view(), name='register'),
    path('user/logout', views.LogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='users'),
]