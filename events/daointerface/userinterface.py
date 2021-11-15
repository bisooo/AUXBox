from events.daointerface.baseinterface import BaseDaoInterface
from events.models.user import User
from django.db import models


class UserDaoInterface(BaseDaoInterface):
    model = User
    def filter_users(self, query: str) -> models.QuerySet:
        """
        query the database for all the Users that contains a part of the search query in their name / username or email
        """
        pass

    def exclude_users_from_event(self, event_id: int) -> models.QuerySet:
        """
        query the database for the users not in an event
        """
        pass

    def get_by_id(self, id: int) -> User:
        """
        query the database for a user by their id
        """
        pass

    def get_by_spotify_id(self, spotify_id: int) -> User:
        """
        query the database for a User identified by their "Refresh Token"
        """
        pass

    def users_in_event(self, event_id) -> models.QuerySet:
        pass

    def create_user(self, first_name: str, last_name: str, username: str, email: str, spotify_id: str):
        """
        method used to create an instance in the database of the User model from the passed validated argument fields
        """
        pass
