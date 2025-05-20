from django.urls import path, include
from rest_framework.routers import DefaultRouter

from parking.views import ParkingSpotView, ParkingRecordView

router = DefaultRouter()
router.register('parking/spots', ParkingSpotView)
router.register('parking/records', ParkingRecordView)

urlpatterns = [
    path('', include(router.urls)),
]
