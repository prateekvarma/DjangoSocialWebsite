from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # commenting custom login view
    #path('login/', views.user_login, name='login'),
    #login and logout default views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
