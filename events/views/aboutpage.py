from django.shortcuts import render
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing


def aboutpage(request):
    """
       Displays AUXBox's ABOUT page.

       **Template:**

       :template:'events/templates/about.html'
    """
    sp = SpotifyHandler()
    user = sp.check_user_authentication(request)

    if not user:
        return landing(request)

    return render(request, 'about.html')
