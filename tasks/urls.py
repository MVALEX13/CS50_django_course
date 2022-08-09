from django.urls import path

# . stands for current directories
from . import views

""" on declare un nom d'app qu'on va utiliser dans les fichiers html """
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]