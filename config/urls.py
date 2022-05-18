from django.contrib import admin
from django.urls import path, include
from pimo.views import OrderViewSet, OfferViewSet, PostViewSet
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='PIMO Swagger')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pimo.urls')),
    path('users/', include('users.urls')),
    path('swagger/', schema_view),
]
