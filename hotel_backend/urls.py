from django.contrib import admin
from django.urls import path, include

# Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger schema setup
schema_view = get_schema_view(
   openapi.Info(
      title="Luxury Hotel API",
      default_version='v1',
      description="API documentation for the Luxury Hotel System",
      contact=openapi.Contact(email="contact@luxuryhotel.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
