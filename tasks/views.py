from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @extend_schema(description="List all tasks")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description="Create a new task", request=None, responses=TaskSerializer
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(description="Retrieve a task by ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(description="Update a task")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(description="Delete a task")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        description="Mark task as complete or incomplete",
        parameters=[
            {
                "name": "completed",
                "description": "true or false",
                "required": True,
                "in": "query",
                "schema": {"type": "boolean"},
            }
        ],
        responses={200: TaskSerializer},
    )
    @action(detail=True, methods=["patch"])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        completed = request.query_params.get("completed")

        if completed is None:
            return Response(
                {"error": "Provide completed=true or completed=false"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task.completed = completed.lower() == "true"
        task.save()
        return Response({"message": "Task updated", "completed": task.completed})
