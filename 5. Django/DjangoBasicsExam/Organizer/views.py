from django.shortcuts import render, redirect
from django.utils import timezone

from Event.models import Event
from Organizer.forms import OrganizerForm
from Organizer.models import Organizer


def create_organizer(request):
    organizer_exists = Organizer.objects.exists()
    if organizer_exists:
        return redirect('organizer_details')

    if request.method == 'POST':
        form = OrganizerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list')
    else:
        form = OrganizerForm()

    context = {
        'form': form,
        'organizer_exists': organizer_exists,
    }
    return render(request, 'create-organizer.html', context)

def organizer_details(request):
    organizer_exists = Organizer.objects.exists()
    if not organizer_exists:
        return redirect('create_organizer')
    organizer = Organizer.objects.first()

    upcoming_events = Event.objects.filter(
        organizer=organizer,
        start_time__gt=timezone.now()
    ).order_by('start_time')

    context = {
        'organizer_exists': organizer_exists,
        'organizer': organizer,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'details-organizer.html', context)

def edit_organizer(request):
    organizer_exists = Organizer.objects.exists()
    if not organizer_exists:
        return redirect('create_organizer')
    organizer = Organizer.objects.first()

    if request.method == 'POST':
        form = OrganizerForm(request.POST, instance=organizer)
        if form.is_valid():
            form.save()
            return redirect('organizer_details')
    else:
        form = OrganizerForm(instance=organizer)

    context = {
        'form': form,
        'organizer_exists': organizer_exists,
        'organizer': organizer,
    }
    return render(request, 'edit-organizer.html', context)

def delete_organizer(request):
    organizer_exists = Organizer.objects.exists()
    if not organizer_exists:
        return redirect('create_organizer')
    organizer = Organizer.objects.first()
    upcoming_events = Event.objects.filter(
        organizer=organizer,
        start_time__gt=timezone.now()
    )
    if request.method == 'POST':
        if not upcoming_events.exists():
            Event.objects.filter(organizer=organizer).delete()
            organizer.delete()
        return redirect('index')
    context = {
        'organizer_exists': organizer_exists,
        'organizer': organizer,
        'has_upcoming': upcoming_events.exists(),
    }
    return render(request, 'delete-organizer.html', context)

