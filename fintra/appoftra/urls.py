from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("packages", views.packages, name="packages"),
    ]