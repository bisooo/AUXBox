from django.shortcuts import render
from django.http import Http404
from django.db.utils import IntegrityError
from tekore import BadRequest
from events.services.user import UserService
from events.services.event import EventService
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing


def homepage(request):
    """
        Displays AUXBox's homepage.

       **Model:**

        A list of all the upcoming Events (:model:'events.Event')

       **Template:**

       :template:'events/templates/home.html'
    """
    sp = SpotifyHandler()

    if request.GET.get('code', False):
        try:
            sp.create_user_token_after_redirect(request)
            UserService.create_user(sp)
            request.session['token'] = sp.user_token.refresh_token
        except IntegrityError:
            UserService.add_new_user_refresh_token(sp)
            request.session['token'] = sp.user_token.refresh_token
        except BadRequest:
            pass

    user = sp.check_user_authentication(request)

    if not user:
        return landing(request)

    events = EventService().get_upcoming_events()

    return render(request, 'home.html', {'events': events})
