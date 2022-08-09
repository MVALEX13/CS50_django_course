# hability to give an Http response
from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Http

#qu'est ce que l'utilisateur voit quand il visit une route particulière

# Create your views here. (views = ce que l'utilisateur va voir)
# je pense que peu importe la requete de l'utilisateur on renvoie hellow world

##### Simple HTTP response functions

""" def index(request):
    return HttpResponse("Hello, world") """

def maxime(request):
    return HttpResponse("hello max")

def david(request):
    return HttpResponse("hello david")

""" def greet(request, name):
    return HttpResponse(f"Hello, {name}") """

""" # fonction capitalize pour mettre premiere lettre en maj
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")
# f for formatted string """


##### entire HTML page response functions

# maintenant si on veut renvoyer quelque chose de plus complet qu'une simple reponse texte http
# si on veut retourner une autre page on utilise la fonction suivante:
# we don't want to render just a string but an entire html file

def index(request):
    return render(request, "hello/index.html")

# on ajoute un dictionnaire python avec le 3 arguments, il s'agit sous forme de key de transmettre une variable pour pour
# personaliser la page, name sera transmise via la variable "name"
# la fonction prend name en argument et le passe au fichier html comme contexte aux données auxquelles le template a accès
def greet(request, name):
    return render(request, "hello/greet.html",{"name": name.capitalize()})


