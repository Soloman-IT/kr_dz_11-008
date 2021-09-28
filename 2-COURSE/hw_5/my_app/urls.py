from django.urls import path
from . import views

urlpatterns = [
	path("", views.main, name = "main"),
	path("news/", views.news, name = "news"),
	path("news/profile/", views.profile, name = "news_profile")
]