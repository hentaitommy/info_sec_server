from django.urls import path
from . import signin_out

urlpatterns = [
    path('signin', signin_out.signin),
    path('signout', signin_out.signout),
    path('userinfo', signin_out.userinfo)
]