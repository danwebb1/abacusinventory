from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework import routers

from api.handlers.inventory_viewset import InventoryViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('inv', InventoryViewSet, basename='Inventory')

urlpatterns = [
    path(r'schema', get_schema_view(title="Abacus Dental Inventory API V1", description="Abacus Dental Inventory Microservice",
                                    version="1.0.0"), name='api-schema'),
]
urlpatterns += router.urls
