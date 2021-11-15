from django.shortcuts import render, redirect, Http404
from django.core.exceptions import ValidationError
from events.models.event import Event
from events.services.event import EventService
from events.forms.event_form import EventForm
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing


def create_event(request):
    """
       Displays a Form to create an Event.

       **Model:**

        Create an instance of an Event (:model:'events.Event').

       **Template:**

       :template:'events/templates/create_event.html'
    """
    sp = SpotifyHandler()
    user = sp.check_user_authentication(request)

    if not user:
        return landing(request)

    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            event = Event()
            event.name = data['title']
            event.spotify_genre = data['spotify_genre']
            event.description = data['description']
            event.location = data['location']
            event.min_request_price = int(data['min_price'])
            event.date = data['date']
            event.time = data['time']
            try:
                event = EventService().create_event_from_form(event)
            except ValidationError as e:
                raise Http404(e)

            return redirect(event)

    return render(request, 'create_event.html', {'form': form})
