from django.db import IntegrityError

from events.factory.DAOFactory import DaoFactory
from events.services.participation import ParticipationService


class InvitationService:
    @staticmethod
    def register_invitation(from_user, to_user, event):
        if not ParticipationService.get_all_participation_in_event(event).filter(user=to_user, event=event).exists():
            return DaoFactory.getInvitationDao().create_invitation(from_user=from_user, to_user=to_user, event=event)
        else:
            raise IntegrityError("MOFO ALREADY JOINED")

    @staticmethod
    def get_users_pending_invitations(user):
        return DaoFactory.getInvitationDao().get_invitations(user=user)
