from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("services", views.services, name="services"),
    path("virtualhr", views.virtualhr, name="virtualhr"),
    path("acservice", views.acservice, name="acservice"),
    path("acservice", views.acservice, name="acservice"),
]