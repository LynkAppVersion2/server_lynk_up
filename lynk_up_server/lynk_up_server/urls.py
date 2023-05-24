"""
URL configuration for lynk_up_server project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.user_list),
    path('users/<int:user_id>', views.user_detail),
    path('users/<int:user_id>/friends/', views.add_friend),
    path('users/<int:user_id>/friends/<int:friend_id>/', views.delete_friend),
    path('groups/', views.group_list),
    path('groups/<int:group_id>/', views.group_detail),
    path('groups/<int:group_id>/delete/', views.group_delete),
    path('groups/<int:group_id>/update/', views.group_update),
    path('groups/create/', views.group_create),
    path('events/', views.event_list),
    path('events/<int:event_id>/', views.event_detail)
]
