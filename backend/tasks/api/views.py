from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView)
from rest_framework.mixins import CreateModelMixin
from tasks.models import Task
from .serializers import TaskSerializer
from django.db.models import Q


class TaskRudView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()


class TaskAPIView(CreateModelMixin, ListAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = Task.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) |
                           Q(description__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
