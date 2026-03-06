from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Taskflow API",
        default_version="v1",
        description="Api documentation for taskflow task management system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="emmanueljoseph.dev.pro@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Task API
    path("admin/", admin.site.urls),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/", include("tasks.urls")),
    # Swagger documentation
    path(
        "swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
