from events.services.invitationresponse import InvitationResponseService
from events.tests import BaseTestCase
from django.db import InternalError


class InvitationResponseTest(BaseTestCase):

    def test_should_accept_invitation(self):
        self.assertTrue(
            InvitationResponseService().accept_invitation(self.mock_from_user, self.mock_to_user, self.mock_event),
            'invitation could not be accepted and participation could not be created')

    def test_should_reject_invitation(self):
        self.assertTrue(
            InvitationResponseService().reject_invitation(self.mock_from_user, self.mock_to_user, self.mock_event),
            'invitation could not be rejected and invitation state could not be adjusted to 0')
