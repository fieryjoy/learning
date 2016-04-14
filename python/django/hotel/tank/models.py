from django.db import models
from django.db.models.signals import post_save, pre_delete

ROOM_TYPES = (
        ('SINGLE', 'single'),
        ('DOUBLE', 'double'),
        ('TRIPLE', 'triple'),
        ('QUAD', 'quad'),
        ('QUEEN', 'queen'),
        ('KING', 'king'),
        ('TWIN', 'twin'),
        ('DOUBLE-DOUBLE', 'double-double'),
        ('STUDIO', 'studio'),
        ('MINI-SUITE', 'mini-suite'),
        ('SUITE', 'suite'),
        )

FORMAL_TITLE = (
        ('Mr', 'Mister'),
        ('Mrs', 'Misses'),
        ('Miss', 'Miss'),
        ('Ms', 'Mizz'),
        )


class Visitor(models.Model):
    title = models.CharField(max_length=20, choices=FORMAL_TITLE, default='Mr')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return "{}. {} {}".format(
                self.title, 
                self.first_name, 
                self.last_name)


class Reservation(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    smoking = models.BooleanField(default=False)
    number_of_rooms = models.IntegerField(default=1)
    confirmed = models.BooleanField(default=False)
    visitor = models.ForeignKey(Visitor, null=True, blank=True, default=None)

    def __str__(self):
        return "Period {}: {}, {}, {}, {}, {}".format(
                self.check_in, self.check_out, 
                self.room_type, self.adults, 
                "smoking" if self.smoking else "non-smoking", 
                "confirmed" if self.confirmed else "not-confirmed")

    def confirm(self):
        self.confirmed = True
        self.save()
        
    def unconfirm(self):
        self.confirmed = False
        self.save()

    def add_visitor(self, visitor):
        self.visitor = visitor
        self.save()


class Room(models.Model):
    room_number = models.IntegerField(default=0, unique=True)
    floor_number = models.IntegerField(default=0)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    reserved = models.BooleanField(default=False)
    reservation = models.ManyToManyField(Reservation, through="RoomReservation")
    smoking = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{}: {}, {}".format(
                self.room_number, 
                self.room_type, 
                "smoking" if self.smoking else "non-smoking")

    def reserve(self):
        self.reserved = True
        self.save()

    def unreserve(self):
        self.reserved = False
        self.save()


class RoomReservation(models.Model):
    room = models.ForeignKey(Room)
    reservation = models.ForeignKey(Reservation)


def room_is_reserved_send_confirmation(sender, instance, **kwargs):
    instance.room.reserve()
    instance.reservation.confirm()

post_save.connect(room_is_reserved_send_confirmation, sender=RoomReservation, dispatch_uid="update_room_reserved")

def room_is_unreserved(sender, instance, **kwargs):
    instance.room.unreserve()
    instance.reservation.unconfirm()

pre_delete.connect(room_is_unreserved, sender=RoomReservation, dispatch_uid="update_room_unreserved")
 
