from django.contrib import admin

from .models import Room, Visitor, Reservation, RoomReservation


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Room Information', {'fields': 
            ['room_number', 'floor_number', 'room_type', 'capacity', 'price', 'smoking', 'reserved']}),
    ]
    list_filter = ['room_type', 'floor_number', 'smoking']
    list_display = ['room_number', 'floor_number', 'room_type', 'reserved', 'smoking']


class VisitorAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name']


class ReservationAdmin(admin.ModelAdmin):
    list_filter = ['confirmed']


class RoomReservationAdmin(admin.ModelAdmin):
    list_display = ['room_id', 'reservation_id']


admin.site.register(Room, RoomAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(RoomReservation, RoomReservationAdmin)
