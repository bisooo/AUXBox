from django.shortcuts import render, redirect
from events.services.spotifyHandler import SpotifyHandler
from events.services.user import UserService
from events.services.friendship import FriendshipService
from events.services.event import EventService
from events.views.landing import landing


def user_search(request, event_id : int):
    """
        A search query for the User's (:model:'events.User') that can be invited

       **Model:**

        A list of the User's (:model:'events.User') that can be invited

       **Template:**

       :template:'events/templates/user_search.html'
    """
    sp = SpotifyHandler()
    user = sp.check_user_authentication(request)

    if not user:
        return landing(request)

    query = request.GET.get('search', '')
    if query:
        users = FriendshipService().filter_friends(user, query)
    else:
        users = None

    event = EventService().get_event_by_id(id=event_id)

    return render(request, 'user_search.html', {'event': event, 'user':user, 'users': users})
