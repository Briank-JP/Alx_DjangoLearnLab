from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterVeiw 

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', RegisterVeiw.as_view(template_name='blog/register.html'), name='register'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
]
