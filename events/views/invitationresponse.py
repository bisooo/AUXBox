from django.shortcuts import render

from events.factory.DAOFactory import DaoFactory
from events.services.invitation import InvitationService
from events.services.spotifyHandler import SpotifyHandler
from events.views.landing import landing
from events.services.invitationresponse import InvitationResponseService


def invitation_response(request, event_id: int, from_user_id: int, to_user_id: int, response: int):
    sp = SpotifyHandler()
    user = sp.check_user_authentication(request)

    if not user:
        return landing(request)

    if response == 1:
        if not InvitationResponseService.accept_invitation(from_user=DaoFactory.getUserDao().get_by_id(from_user_id),
                                                           to_user=DaoFactory.getUserDao().get_by_id(to_user_id),
                                                           event=DaoFactory.getEventDao().find_by_id(event_id)):
            warning = "invitation could not be accepted and participation could not be created"
        else:
            warning = ""

    else:
        if not InvitationResponseService.reject_invitation(from_user=DaoFactory.getUserDao().get_by_id(from_user_id),
                                                           to_user=DaoFactory.getUserDao().get_by_id(to_user_id),
                                                           event=DaoFactory.getEventDao().find_by_id(event_id)):
            warning = "invitation could not be rejected and invitation state could not be adjusted to 0"
        else:
            warning = ""

    invitations = InvitationService.get_users_pending_invitations(user=user)

    return render(request, 'invites.html', {'invitations': invitations, 'warning': warning})
