from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.utils.timezone import now
from django.db.models.deletion import Collector


User = get_user_model()


class Room(models.Model):
    name = models.CharField('Кабинет', max_length=100)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name='Комната', on_delete=models.CASCADE)
    start_time = models.DateTimeField('Начало', null=True)
    end_time = models.DateTimeField('Конец', null=True)

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Журнал бронирования'

    def __str__(self):
        return f"{self.user.username} - {self.room.name} - {self.start_time}"


