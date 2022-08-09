from django.urls import path

# . stands for current directories
from . import views

urlpatterns = [
    #"" for no additionnal argument, quand qq visite cet url "", empty url
    # views.index : what view should be rended when url is visited
    path("", views.index, name = "index"),
    path("maxime", views.maxime, name="maxime"),
    path("david", views.david, name ="david"),
    #le string que je rentre dans ma barre de recherche est affecté à l'argument 'name' de la fonction views.greet
    # adaptable/fonctionne avec tous les noms
    path("<str:name>", views.greet, name="greet"),
]

# "<str:name> : "quand j'ai un url qui est un string (quelcqonque) on appelle la fonction views.greet"