from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vehicles.views import VehicleTypeView, VehicleView

router = DefaultRouter()
router.register('vehicles/type', VehicleTypeView)
router.register('vehicles', VehicleView)

urlpatterns = [
    path('', include(router.urls)),
]