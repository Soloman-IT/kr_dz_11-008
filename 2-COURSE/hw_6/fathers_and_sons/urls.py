from django.urls import path
from . import views

urlpatterns = [path("", views.main, name = "main"),
               path("/dop_1/", views.dop_page_1, name = "dop_1"),
               path("/dop_2", views.dop_page_2, name = "dop_2")]
