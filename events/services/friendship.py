from django.db.models import QuerySet

from events.dao.friendship import FriendshipDao
from events.models.user import User
from events.factory.DAOFactory import DaoFactory
from events.services.spotifyHandler import SpotifyHandler


class FriendshipService:

    def get_user_friendships(user):
        return DaoFactory.getFriendshipDao().get_friendships(user_id=user)

    def get_accepted_user_friendships(user):
        return DaoFactory.getFriendshipDao().get_accepted_friendships(user_id=user)

    def get_rejected_user_friendships(user):
        return DaoFactory.getFriendshipDao().get_rejected_friendships(user_id=user)

    @staticmethod
    def filter_friends(user, query :str):
        return DaoFactory.getFriendshipDao().filter_users(user, query)
