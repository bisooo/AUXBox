from events.daointerface.baseinterface import BaseDaoInterface
from events.models.comment import Comment


class CommentDaoInterface(BaseDaoInterface):

    model = Comment
