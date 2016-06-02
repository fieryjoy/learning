from datetime import date, datetime
from django import forms
from django.db import models
from django.forms.utils import ErrorList
from tank.models import Reservation, Room, Visitor, RoomReservation
from django.db.models import Q
from itertools import chain


def make_custom_datefield(f, **kwargs):
    formfield = f.formfield(**kwargs)
    if isinstance(f, models.DateField):
        formfield.widget.format = '%m/%d/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield


class ReservationForm(forms.ModelForm):
    formfield_callback = make_custom_datefield

    class Meta:
        model = Reservation
        fields = ('check_in', 'check_out', 'room_type', 'adults', 'children', 'smoking', 'number_of_rooms',)
        widgets = {
            'check_in': forms.DateInput(format='%Y-%m-%d', attrs={'class':'datePicker', 'readonly':'true'}),
            'check_out': forms.DateInput(format='%Y-%m-%d', attrs={'class':'datePicker', 'readonly':'true'}),
        } 

    def check_availability(self):
        check_in = self.cleaned_data['check_in']        
        check_out = self.cleaned_data['check_out']
        if check_in > check_out:
            self.errors['about_dates'] = ErrorList(['check_in date has to be before check_out date'])
        if check_in < date.today():
            self.errors['about_dates'] = ErrorList(['check_in date should not be in the past'])
 
        room_type = self.cleaned_data['room_type']
        adults = self.cleaned_data['adults']
        smoking = self.cleaned_data['smoking']
        number_of_rooms = self.cleaned_data['number_of_rooms']

        free_rooms_qs = Room.objects.none()
        confirmed_reservations = Reservation.objects.exclude(confirmed=True)
        # filter by room_type and smoking
        rooms_qs = Room.objects.filter(room_type=room_type, smoking=smoking)
        # exclude already reserved rooms (TODO: filter by dates)
        rooms_without_reservations_qs = rooms_qs.exclude(reservation__in=confirmed_reservations)
        if len(rooms_without_reservations_qs) == 0:
            reserved_rooms_qs = rooms_qs.filter(reservation__in=confirmed_reservations)
            free_rooms_qs = reserved_rooms_qs.exclude(
                    Q(reservation__check_in__in=[check_in, check_out])
                    |
                    Q(reservation__check_out__in=[check_in, check_out]))
            if len(free_rooms_qs) == 0:
                self.errors['about_reservation'] = ErrorList([u'No rooms available'])
        else:
            rooms_qs = chain(rooms_without_reservations_qs, free_rooms_qs)
        return list(rooms_qs)


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'

    def check_if_already_exists(self):
        email = self.data['email']
        try:
            visitor = Visitor.objects.get(email=email)
        except:
            visitor = None
        return visitor
