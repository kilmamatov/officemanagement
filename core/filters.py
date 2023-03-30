import django_filters
from core import models


class Room(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.Room
        fields = '__all__'


class Booking(django_filters.FilterSet):
    room = django_filters.CharFilter(field_name='room', lookup_expr='icontains')

    class Meta:
        model = models.Booking
        fields = '__all__'
