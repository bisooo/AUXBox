from django.shortcuts import render
from events.services.event import EventService
from events.services.participation import ParticipationService
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing


def view_event(request, event_id : int):
    """
       Displays an individual Event page.

       **Model:**

        An instance of an Event :model:'events.Event'.

        A list of the User (:model:'events.User') participants (:model:'events.Participation')

       **Template:**

       :template:'events/templates/event.html'
    """
    sp = SpotifyHandler()
    user = sp.check_user_authentication(request)

    if not user:
        return landing(request)

    event = EventService().get_event_by_id(id=event_id)
    participation = ParticipationService().get_all_participation_in_event(event_id=event_id)

    return render(request, 'event.html', {'event': event, 'participation': participation})
