from rest_framework import serializers
from core import models


class UserProfile(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ['nickname', 'phone']


class Room(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = ['name']


class Booking(serializers.ModelSerializer):
    room = Room()
    userprofile = UserProfile()

    class Meta:
        model = models.Booking
        exclude = ['user', 'id']


# class Booking(serializers.Serializer):
#     display = serializers.SerializerMethodField()
#
#     class Meta:
#         model = models.Booking
#         fields = '__all__'
#         # exclude = ['name']
#
#     def get_display(self, obj: models.Tag) -> str:
#         return f'{obj.id}. {obj.name}'

