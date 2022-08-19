"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from proyecto1.views import saludo #Se importa la vista
from proyecto1.views import despedida #Se importa la vista
from proyecto1.views import dameFecha #Se importa la vista
from proyecto1.views import calculaEdad #Se importa la vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), # Se especifica el path y la vista (Que esta en views)
    path('nosvemos/', despedida), # Se especifica el path y la vista (Que esta en views)
    path('fecha/', dameFecha),
    path('edades/<int:edad>/<int:agno>', calculaEdad)
]
