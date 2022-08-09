""" outils django pour faciliter la creation de forms """
from http.client import HTTPResponse
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render

import tasks

""" global variable accessible pour tout le monde qui se connecte a l'appli """
## tasks = ["foo", "bar", "baz"]


# Create your views here.
def index(request):
    """ je regarde dans la session pour voir si il ya deja une liste de taches, si il n'y en a pas j'endeclare une nouvelle """
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        ## "tasks":tasks
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        """ request.POST contient toutes les données que l'utilisateur a soumis lorsque il a soumis le form """
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            ## tasks.append(task) ## fonctionne que lorsque liste globale
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form":form
            })

    return render(request, "tasks/add.html", {
        "form":NewTaskForm()
    })

## new class NewTaskForm that inherit from forms.form
class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    priority = forms.IntegerField(label ="priority", min_value=1, max_value=10)

""" Les methodes de la classe form permettent de generer automatiquement du code html """
