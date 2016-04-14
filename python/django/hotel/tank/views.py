from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.template.context_processors import csrf

from tank.forms import ReservationForm, VisitorForm
from tank.models import Room, Visitor, Reservation

def index(request):
    context = {}
    return render(request, 'tank/index.html', context)

def success(request):
    context = {}
    return render(request, 'tank/success.html', context)

def failed(request):
    context = {}
    return render(request, 'tank/failed.html', context)

def detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    context = {'room': room}
    return render(request, 'tank/detail.html', context)

def add_reservation(request):
    context = {}
    initial = {'reservation_id': request.session.get('reservation_id', None)}
    if request.method == 'POST':
        form = ReservationForm(request.POST, initial)
        if form.is_valid():
            results = form.check_availability()
            if results:
                reservation = form.save(commit=True)
                request.session['reservation_id'] = reservation.id
                return HttpResponseRedirect(reverse('add_visitor'))
    else:
        form = ReservationForm()
    context.update(csrf(request))
    context['form'] = form
    return render(request, 'tank/add_reservation.html', context)

def add_visitor(request):
    context = {}
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=True)
        else:
            visitor = form.check_if_already_exists()
        if visitor:
            reservation_id = request.session['reservation_id']
            if reservation_id:
                try:
                    reservation = Reservation.objects.get(id=reservation_id)
                except:
                    return HttpResponseRedirect(reverse('failed'))
                reservation.add_visitor(visitor)
                return HttpResponseRedirect(reverse('success'))
            return HttpResponseRedirect(reverse('failed'))
    else:
        form = VisitorForm()
    context.update(csrf(request))
    context['form'] = form
    return render(request, 'tank/add_visitor.html', context)

