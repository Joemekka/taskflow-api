from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

task_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=["title"],
    properties={
        "title": openapi.Schema(
            type=openapi.TYPE_STRING, example="Finish Capstone Project"
        ),
        "description": openapi.Schema(
            type=openapi.TYPE_STRING, example="Complete the backend implementation"
        ),
        "completed": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
    },
)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @swagger_auto_schema(operation_description="List all tasks")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new task", request_body=task_example
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a task by ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a task")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a task")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Mark task as complete or incomplete",
        manual_parameters=[
            openapi.Parameter(
                "completed",
                openapi.IN_QUERY,
                description="true or false",
                type=openapi.TYPE_BOOLEAN,
            )
        ],
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
