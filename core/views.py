from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import GenericAPIView
from core import models, serializers, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, IsAdminUser
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group


class RegisterUser(GenericAPIView):
    queryset = models.User
    serializer_class = serializers.RegisterUser

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = models.User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],

        )
        user.groups.add(Group.objects.get(name='CRUD'))
        token = Token.objects.create(user=user)
        return Response({'token': token.key})


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
    serializer_class = serializers.BookingCRUD
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Booking

    def get_queryset(self):
        return models.Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


# def room(request):
#     search_serializer = serializers.Room(data=request.GET)
#     if not search_serializer.is_valid():
#         return JsonResponse(search_serializer.errors, status=400)
#     f = filters.Room(request.GET, queryset=models.Room.objects.all())
#     serializer = serializers.Room(instance=f.qs, many=True)
#     return JsonResponse({'results': serializer.data})


