from django.shortcuts import render, redirect, get_object_or_404

from Event.forms import EventForm
from Event.models import Event
from Organizer.models import Organizer


def index(request):
    organizer_exists = Organizer.objects.exists()
    context = {
        'organizer_exists': organizer_exists,
    }
    return render(request, 'index.html', context)

def events_list(request):
    organizer_exists = Organizer.objects.exists()
    events = Event.objects.order_by('-start_time')
    context = {
        'organizer_exists': organizer_exists,
        'events': events,
        'event_count': events.count(),
    }
    return render(request, 'events.html', context)

def create_event(request):
    organizer_exists = Organizer.objects.exists()
    if not organizer_exists:
        return redirect('create_organizer')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = Organizer.objects.first()
            event.save()
            return redirect('events_list')
    else:
        form = EventForm()

    context = {
        'form': form,
        'organizer_exists': organizer_exists,
    }
    return render(request, 'create-event.html', context)

def event_details(request, pk):
    organizer_exists = Organizer.objects.exists()
    event = get_object_or_404(Event, pk=pk)
    formatted_start_time = event.start_time.strftime("%a %d %b %Y %H:%M")
    context = {
        'organizer_exists': organizer_exists,
        'event': event,
        'formatted_start_time': formatted_start_time,
    }
    return render(request, 'details-event.html', context)

def edit_event(request, pk):
    organizer_exists = Organizer.objects.exists()
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_details', pk=event.pk)
    else:
        form = EventForm(instance=event)

    context = {
        'form': form,
        'organizer_exists': organizer_exists,
        'event': event,
    }
    return render(request, 'edit-event.html', context)

def delete_event(request, pk):
    organizer_exists = Organizer.objects.exists()
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        event.delete()
        return redirect('events_list')

    context = {
        'organizer_exists': organizer_exists,
        'event': event,
    }
    return render(request, 'delete-event.html', context)