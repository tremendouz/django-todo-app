from django.conf.urls import re_path

from .views import TaskRudView, TaskAPIView

app_name = 'tasks'
urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', TaskRudView.as_view(), name='task-rud'),
    re_path(r'^$', TaskAPIView.as_view(), name='task-create')

]
