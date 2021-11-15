from events.factory.DAOFactory import DaoFactory
from django.db import InternalError


class InvitationResponseService:

    @staticmethod
    def accept_invitation(from_user, to_user, event):
        DaoFactory.getInvitationDao().accept_invitation(from_user, to_user, event)
        if not DaoFactory.getInvitationDao().check_invitation(from_user, to_user, event, 1):
            return False
        DaoFactory.getParticipationDao().create_participation(to_user, event)
        if not DaoFactory.getParticipationDao().check_participation(event.id, to_user.id):
            return False
        return True

    @staticmethod
    def reject_invitation(from_user, to_user, event):
        DaoFactory.getInvitationDao().reject_invitation(from_user, to_user, event)
        if not DaoFactory.getInvitationDao().check_invitation(from_user, to_user, event, 0):
            return False
        if DaoFactory.getParticipationDao().check_participation(event.id, to_user.id):
            return False
        return True

