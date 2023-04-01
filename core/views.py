from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import GenericAPIView
from core import models, serializers, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAdminUser
from rest_framework.decorators import action


# class RegisterUser(GenericAPIView):
#     queryset = models.User
#     serializer_class = serializers.RegisterUser
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         models.User.objects.create_user(
#             username=
#         )


class RoomViewSet(ReadOnlyModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.Room
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Room


class BookingViewSet(ReadOnlyModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.Booking
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Booking


class RoomCrudViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser,)
    queryset = models.Room.objects.all()
    serializer_class = serializers.Room
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Room


class BookingCrudViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    serializer_class = serializers.Booking
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Booking

    def get_queryset(self):
        return models.Booking.objects.filter(user=self.request.user)


# def room(request):
#     search_serializer = serializers.Room(data=request.GET)
#     if not search_serializer.is_valid():
#         return JsonResponse(search_serializer.errors, status=400)
#     f = filters.Room(request.GET, queryset=models.Room.objects.all())
#     serializer = serializers.Room(instance=f.qs, many=True)
#     return JsonResponse({'results': serializer.data})


