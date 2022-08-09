"""cours_Django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# define what urls I can access
urlpatterns = [
    path('admin/', admin.site.urls),
    
    #after you added the path "hello" i want you to add all the hello personnal files
    # une fois que python est sur l'application hello on lui indique de regarder les autres urls propres à l'application hello
    path('hello/', include("hello.urls")),
    path('newyear/', include('newyear.urls')),
    path('tasks/', include('tasks.urls')),
]

# path('quand quelqu'un visite ça','j'exécute ça', un nom)
# urls are the table of contents for my entire application