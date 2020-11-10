from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # commenting custom login view
    #path('login/', views.user_login, name='login'),
    #login and logout default views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    #following path takes care of all password resets and change
    path('', include('django.contrib.auth.urls')),
    #hand coded password paths for above
    # change password urls (user needs to be logged in)
    #path('password_change/', auth_views.PasswordChangeView.as_view(),name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls (user does NOT need to be logged in)
    #path('password_reset/',
        #auth_views.PasswordResetView.as_view(),
        #name='password_reset'),
    #path('password_reset/done/',
        #auth_views.PasswordResetDoneView.as_view(),
        #name='password_reset_done'),
    #path('reset/<uidb64>/<token>/',
        #auth_views.PasswordResetConfirmView.as_view(),
        #name='password_reset_confirm'),
    #path('reset/done/',
        #auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #hand coded password paths end

    path('register/', views.register, name='register'),
]
