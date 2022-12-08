from django.urls import path

from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("accounts/login/", LoginView.as_view(), name='accounts/login')
]
