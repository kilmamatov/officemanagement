from django.contrib import admin
from core import models


@admin.register(models.Room)
class Room(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Booking)
class Booking(admin.ModelAdmin):
    list_display = ('room', 'start_time', 'end_time')


@admin.register(models.UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('phone', 'nickname')


