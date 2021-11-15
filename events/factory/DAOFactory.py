from events.dao.base import BaseDao
from events.dao.collaboration import CollaborationDao
from events.dao.comment import CommentDao
from events.dao.event import EventDao
from events.dao.friendship import FriendshipDao
from events.dao.host import HostDao
from events.dao.invitation import InvitationDao
from events.dao.participation import ParticipationDao
from events.dao.request import RequestDao
from events.dao.upvote import UpvoteDao
from events.dao.user import UserDao


class DaoFactory:

    @staticmethod
    def getBaseDao():
        return BaseDao()

    @staticmethod
    def getCollaborationDao():
        return CollaborationDao()

    @staticmethod
    def getCommentDao():
        return CommentDao()

    @staticmethod
    def getEventDao():
        return EventDao()

    @staticmethod
    def getHostDao():
        return HostDao()

    @staticmethod
    def getInvitationDao():
        return InvitationDao()

    @staticmethod
    def getParticipationDao():
        return ParticipationDao()

    @staticmethod
    def getRequestDao():
        return RequestDao()

    @staticmethod
    def getUpvoteDao():
        return UpvoteDao()

    @staticmethod
    def getUserDao():
        return UserDao()

    @staticmethod
    def getFriendshipDao():
        return FriendshipDao()
