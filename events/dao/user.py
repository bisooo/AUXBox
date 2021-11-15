from events.dao.base import BaseDao
from events.models.user import User
from django.db import models
from django.db.models import Q
from events.daointerface.userinterface import UserDaoInterface



class UserDao(BaseDao, UserDaoInterface):
    model = User

    def filter_users(self, query: str) -> models.QuerySet:
        """
        DAO method used to query the database for all the Users that contains a part of the search query in their name / username or email

        :param query: the string search query

        :return: a set of all the User model objects
        """
        return self.model.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query) | Q(
                email__icontains=query))

    def get_by_id(self, id: int) -> User:
        """
        DAO method used to query the database for a User identified by their "ID"

        :param id: the primary key "ID" of a User

        :return: a User model object
        """
        return self.model.objects.get(id=id)

    def get_by_spotify_id(self, spotify_id: int) -> User:
        """
        DAO method used to query the database for a User identified by their "Refresh Token"

        :param spotify_id: the refresh token of a User

        :return: a User model object
        """
        return self.model.objects.get(spotify_id=spotify_id)

    def users_in_event(self, event_id) -> models.QuerySet:
        """
        DAO method used to query the database for all the Users that are "participants" of the specified Event "ID"

        :param event_id: the primary key "ID" of an Event

        :return: a set of all the User model objects
        """
        return self.model.objects.filter(participation__event_id=event_id).all()

    def exclude_users_from_event(self, event_id: int) -> models.QuerySet:
        """
        DAO method used to query the database for all the Users that are not "participants" of the specified Event "ID"

        :param event_id: the primary key "ID" of an Event

        :return: a set of all the User model objects
        """
        return self.model.objects.exclude(participation__event_id=event_id).all()

    def create_user(self, first_name: str, last_name: str, username: str, email: str, spotify_id: str):
        """
                DAO method used to create an instance in the database of the User model from the passed validated
                argument fields

                :param first_name: first name of the user
                :param last_name: last name of the user
                :param username: username chosen by the user
                :param email: email acquired from the spotify account
                :param spotify_id: ID from the user's spotify account

                :return: an User model object
        """
        return self.model.objects.create(first_name=first_name,
                                         last_name=last_name,
                                         username=username,
                                         email=email,
                                         spotify_id=spotify_id)
