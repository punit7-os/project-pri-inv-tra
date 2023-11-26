from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("services", views.services, name="services"),
    path("know-more/<int:mid>", views.info, name="know-more"),
    path("about", views.about, name="about"),
    # path("acservice", views.acservice, name="acservice"),
]