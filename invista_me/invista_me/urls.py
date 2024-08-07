"""
URL configuration for invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from invista_me2 import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.investimentos_funcao,name='investimentos'),  # pagina inicial
    path('politica/',views.politica_privacidade,name='politica'),
    path('novo/',views.criar,name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>',views.editar,name='editar'),
    path('excluir_investimento/<int:id_investimento>', views.excluir,name='excluir'),
    path('/<int:id_investimento>',views.detalhe,name='detalhe'),
   

]
