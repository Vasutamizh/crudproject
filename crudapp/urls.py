"""
URL configuration for crud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views


urlpatterns = [
    path('index/', views.home , name='index'),
    path('add_employee/', views.add_employee, name='add'),
    path('list/',  views.read, name='read'),
    path('update/<id>/', views.update, name='update'),
    path('delete/<id>/', views.delete, name='delete'),
    # authentication
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
   # path('logout/', views.user_logout, name='logout'),
]
