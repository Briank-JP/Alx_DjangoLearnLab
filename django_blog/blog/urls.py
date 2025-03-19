from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterVeiw, profile
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', RegisterVeiw.as_view(template_name='blog/register.html'), name='register'),
    path('profile/', profile, name='profile'),
    # urls for crud operations
    path('',PostListView.as_view(), name = 'posts_home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    ]
