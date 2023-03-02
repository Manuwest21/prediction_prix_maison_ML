"""estimation URL Configuration

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
from django.urls import path
from immo_prix import views
from immo_prix.views import HomeView, ResultView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('estimer/', views.estimer, name='estimer'),
    
    #path('rslt_estimation/', ResultView.as_view (), name='rslt_estimation')
    # path('rslt_estimation/', views.rslt_estimation, name='rslt_estimation'),
    path('rslt_estimation/', views.rslt_estimation, name='rslt_estimation'),
    # path('estimer/rslt_estimation/', views.rslt_estimation, name='rslt_estimation'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('infos_form', views.infos_form, name='infos_form')
]
