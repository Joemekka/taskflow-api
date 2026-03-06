from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import responses


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
