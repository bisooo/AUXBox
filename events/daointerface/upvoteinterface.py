from events.daointerface.baseinterface import BaseDaoInterface
from events.models.upvote import Upvote


class UpvoteDaoInterface(BaseDaoInterface):

    model = Upvote
