from events.dao.base import BaseDao
from django.db import models, IntegrityError
from events.models.invitation import Invitation
from events.daointerface.invitationinterface import InvitationDaoInterface
from django.db.models import Q


class InvitationDao(BaseDao, InvitationDaoInterface):
    model = Invitation

    def get_invitations(self, user):
        return self.model.objects.filter(Q(to_user=user, state=2))

    def accept_invitation(self, from_user, to_user, event):
        return self.model.objects.filter(from_user=from_user, to_user=to_user, event=event).update(state=1)

    def reject_invitation(self, from_user, to_user, event):
        return self.model.objects.filter(from_user=from_user, to_user=to_user, event=event).update(state=0)

    def create_invitation(self, from_user, to_user, event):
        if not (self.model.objects.filter(Q(from_user=from_user) & Q(to_user=to_user) & Q(event=event)).exists()):
            return self.model.objects.create(from_user=from_user, to_user=to_user, event=event, state=2)
        else:
            raise IntegrityError("YOU ALREADY INVITED THIS MOFO")

    def check_invitation(self, from_user, to_user, event, state):
        return self.model.objects.filter(from_user=from_user, to_user=to_user, event=event, state=state).exists()
