"""
URL configuration for bulk_mail project.

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
from django.shortcuts import redirect
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name="index"),
    path('create-contact/', create_user, name="create_contact"),
    path('view_contacts/', view_contacts, name="view_contacts"),
    path('view_groups/', view_groups, name="view_groups"),
    path('create_group/', create_group, name="create_group"),
    path('group/<int:id>/', group_detail, name='group'),
    path('emailsent/<int:id>/',sent_success,name="sent_success"),
]
