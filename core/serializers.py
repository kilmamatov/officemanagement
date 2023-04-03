from rest_framework import serializers
from core import models


class Room(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = ['name']


class Booking(serializers.ModelSerializer):
    room = Room()

    class Meta:
        model = models.Booking
        exclude = ['id']
        # fields = '__all__'


class BookingCRUD(serializers.ModelSerializer):

    class Meta:
        model = models.Booking
        exclude = ['user', 'id']
        # fields = '__all__'


class RegisterUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if models.User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Такое имя уже занято')
        return value



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

