from events.daointerface.baseinterface import BaseDaoInterface
from events.models.invitation import Invitation


class InvitationDaoInterface(BaseDaoInterface):

    model = Invitation
