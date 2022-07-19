from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# DRF Yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='galeria api',
        default_version='v1',
        description='api de galeria',
        contact=openapi.Contact(email='support@books.com'),
        license=openapi.License(name="bsd licnse")
    ),
    public=True
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('arte_artista.urls')),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
