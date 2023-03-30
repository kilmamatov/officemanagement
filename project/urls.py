from django.contrib import admin
from django.urls import path, include
from core import urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    path('', include(urls)),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
]
