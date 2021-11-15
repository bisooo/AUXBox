from django.shortcuts import render
from events.services.user import UserService
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing


def profile(request):
     """
       Displays User's Profile page.

       **Template:**

       :template:'events/templates/profile.html'
    """

     sp = SpotifyHandler()
     user = sp.check_user_authentication(request)

     if not user:
          return landing(request)

     return render(request, 'profile.html', {'user': user})
