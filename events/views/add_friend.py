from django.db import IntegrityError
from django.shortcuts import render, redirect

from events.services.invitation import InvitationService
from events.services.user import UserService
from events.services.event import EventService
from events.models.participation import Participation
from events.services.participation import ParticipationService
from events.dao.participation import ParticipationDao
from events.factory.DAOFactory import DaoFactory
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing


def add_friend(request, event_id: int, user_id: int):
    """
       Displays the updated list of friends that can be invited to an Event.

       **Model:**

        A list of the User's (:model:'events.User') that can be invited

       **Template:**

       :template:'events/templates/user_search.html'
    """
    sp = SpotifyHandler()
    user = sp.check_user_authentication(request)
    to_user = UserService.get_user_by_id(id=user_id)

    if not user:
        return landing(request)

    event = EventService().get_event_by_id(id=event_id)

    try:
        InvitationService().register_invitation(from_user=user, to_user=to_user, event=event)

    except Exception as e:
        warning = e
        return render(request, 'user_search.html', {'event': event, 'warning': warning})
    warning = ""

    return render(request, 'user_search.html', {'event': event, 'warning': warning})
