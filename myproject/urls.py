"""myproject URL Configuration
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

# lets define a view function
#from views import myHomeViewFunction,myAboutUsViewFunction,myContactUsViewFunction
from . import views

urlpatterns = [ # List
    path('shalu/', admin.site.urls,name="adminRoute"),
    #path(route, view, kwargs=None, nameOfTheRoute=None)
    path('', views.myHomeViewFunction , name="homeRoute" ),
    path('aboutus/', views.myAboutUsViewFunction , name="aboutUsoute" ),
    path('contactus/', views.myContactUsViewFunction , name="contactUsRoute" ),
    path('product/<slug:category>',views.category,name="categoryRoute"),
]
