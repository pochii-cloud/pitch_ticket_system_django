from django.urls import path

from account.views import RegisterUser, LoginPage, AdminLogin, LogoutPage

urlpatterns = [
    path('RegisterUser/', RegisterUser.as_view(), name='RegisterUser'),
    path('LoginPage/', LoginPage.as_view(), name='LoginPage'),
    path('LogoutPage/', LogoutPage.as_view(), name='LogoutPage'),
    path('AdminLogin/', AdminLogin.as_view(), name='AdminLogin'),
]
