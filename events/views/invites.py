from django.shortcuts import render

from events.services.invitation import InvitationService
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing


def invites(request):
    """
       Displays User's Invites page.

       **Template:**

       :template:'events/templates/invites.html'
    """
    sp = SpotifyHandler()
    user = sp.check_user_authentication(request)
    invitations = InvitationService.get_users_pending_invitations(user=user)


    if not user:
        return landing(request)

    return render(request, 'invites.html', {'invitations': invitations})
