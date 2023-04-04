from django.urls import path
from rest_framework.routers import DefaultRouter
import core.views

urlpatterns = [
    path('register_user/', core.views.RegisterUser.as_view()),
    path('login_user/', core.views.LoginUser.as_view())
]

router = DefaultRouter()
router.register('rooms', core.views.RoomViewSet, basename='room')
router.register('bookings', core.views.BookingViewSet, basename='booking')
router.register('roomsCrud', core.views.RoomCrudViewSet, basename='roomCrud')
router.register('bookingsCrud', core.views.BookingCrudViewSet, basename='bookingCrud')
urlpatterns += router.urls
