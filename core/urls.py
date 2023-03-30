from django.urls import path
from rest_framework.routers import DefaultRouter
import core.views

urlpatterns = [
]

router = DefaultRouter()
router.register('rooms', core.views.RoomViewSet, basename='room')
router.register('bookings', core.views.BookingViewSet, basename='booking')
router.register('roomsСrud', core.views.RoomCrudViewSet, basename='roomCrud')
router.register('bookingsCrud', core.views.BookingCrudViewSet, basename='bookingCrud')
urlpatterns += router.urls
