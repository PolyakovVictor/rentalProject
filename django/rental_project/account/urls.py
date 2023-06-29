from django.urls import path
from django.contrib.auth import views
from django.views.generic import TemplateView

from . import views as my_views


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='login.html',), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    path('password_change/', views.PasswordChangeView.as_view(), name="password_change"),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', views.LogoutView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', views.LogoutView.as_view(), name="password_reset_confirm"),
    path('reset/done/', views.LogoutView.as_view(), name="password_reset_done"),

    path('register', my_views.Register.as_view(), name="register"),

    path('', TemplateView.as_view(template_name='home.html'), name="home")
]
