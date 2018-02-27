"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.urls import re_path


from tasks.views import (home, HomeView, HomeTemplateView,
                         tasks_listview, SearchTaskListView, TaskDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^$', home),
    #path('', HomeView.as_view())
    #re_path(r'^tasks/(?P<pk>\w+)/$', TaskDetailView.as_view()),
    path('tasks/', tasks_listview),
    re_path(r'^tasks/(?P<slug>\w+)/$', SearchTaskListView.as_view()),
    path('', HomeTemplateView.as_view()),
    re_path(r'^api/tasks/', include('tasks.api.urls', namespace="api-tasks")),
]
