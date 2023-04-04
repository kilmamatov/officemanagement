from rest_framework import serializers
from core import models


class User(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username']


class Room(serializers.ModelSerializer):

    class Meta:
        model = models.Room
        fields = ['name']


class Booking(serializers.ModelSerializer):
    room = Room()
    user = User()

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


class LoginUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if not models.User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем не найден')
        return value

    def validate(self, attrs):
        user = models.User.objects.get(username=attrs['username'])
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError({'password': 'Пароль не верный'})
        return attrs


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

