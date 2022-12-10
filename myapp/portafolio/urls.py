from django.urls import path

from . import views


urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("portafolio/", views.PortafolioView.as_view(), name='portafolio'),
    path("portafolio/add", views.PortafolioAdd.as_view(), name='portafolio_add'),
]
