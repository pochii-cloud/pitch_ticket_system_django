from django.urls import path

from account.views import RegisterUser

urlpatterns = [
    path('RegisterUser/', RegisterUser.as_view(), name='RegisterUser')
]
