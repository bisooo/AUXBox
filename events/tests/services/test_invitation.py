from django.db import IntegrityError

from events.factory.DAOFactory import DaoFactory
from events.services.invitation import InvitationService
from events.tests import BaseTestCase


class InvitationTestCase(BaseTestCase):

    def test_existing_user_invitation(self):
        with self.assertRaisesMessage(IntegrityError, "YOU ALREADY INVITED THIS MOFO"):
            InvitationService().register_invitation(self.user, self.user2, self.event2.id)

    def test_existing_user(self):
        with self.assertRaisesMessage(IntegrityError, "MOFO ALREADY JOINED"):
            InvitationService().register_invitation(self.user, self.user3, self.event2.id)

    def test_invitation_exists(self):
        InvitationService().register_invitation(self.user3, self.user, self.event2)
        self.assertEqual(DaoFactory.getInvitationDao().get_invitations(self.user).exists(), True)
