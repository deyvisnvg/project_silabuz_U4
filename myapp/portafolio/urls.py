from django.urls import path

from . import views


urlpatterns = [
    path("portafolio/", views.PortafolioView.as_view(), name='portafolio')
]
