from django.urls import path
from . import views

urlpatterns = [path("", views.main, name="main"),
               path("dop_1", views.dop_page_1, name="dop_1"),
               path("dop_2", views.dop_page_2, name="dop_2"),
               path('list_objects', views.lst_obj, name='lst_obj'),
               path('delete/<int:id_message>', views.delete, name='del'),
               path('choice_edit/<int:id_message>', views.choice_edit, name='ch_ed'),
               path('choice_delete/<int:id_message>', views.choice_del, name='ch_del'),
               path('edit/<int:id_message>', views.edit, name='ed')]
