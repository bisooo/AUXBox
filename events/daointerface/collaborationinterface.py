from events.daointerface.baseinterface import BaseDaoInterface
from events.models.collaboration import Collaboration


class CollaborationDaoInterface(BaseDaoInterface):

    model = Collaboration
