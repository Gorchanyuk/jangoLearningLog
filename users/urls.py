from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    #Страница входа
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    #path('logout/', views.logout_view, name='logout'),
    path('logout/', LogoutView.as_view(next_page='learning_logs:index'), name='logout'),
    #Страница регистрации
    path('register/', views.register, name='register'),
]