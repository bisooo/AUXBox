from django.db.models import QuerySet
from events.models.user import User
from events.factory.DAOFactory import DaoFactory
from events.services.spotifyHandler import SpotifyHandler


class UserService:

    @staticmethod
    def search_users(query: str) -> QuerySet:
        """
        Service method used to filter and return a set of Users based on a search query

        :param query: the string search query

        :return: set of all the User model objects
        """
        return DaoFactory.getUserDao().filter_users(query)

    @staticmethod
    def get_all_users_not_in_event(event_id: int) -> QuerySet:
        """
        Service method used to get all the Users which are not "participants" of an Event

        :param event_id: the primary key "ID" of an Event model

        :return: set of all the User model objects
        """
        return DaoFactory.getUserDao().exclude_users_from_event(event_id=event_id)

    @staticmethod
    def get_all_users_in_event(event_id: int) -> QuerySet:
        return DaoFactory.getUserDao().users_in_event(event_id=event_id)

    @staticmethod
    def get_user_by_id(id: int) -> User:
        """
        Service method used to query the database for a User identified by their "ID"

        :param id: the primary key "ID" of a User

        :return: a User model object
        """
        return DaoFactory.getUserDao().get_by_id(id=id)

    @staticmethod
    def get_user_by_spotifyid(spotifyid: str) -> User:
        """
        Service method used to query the database for a User identified by their "SpotifyID"

        :param spotifyid: the "SpotifyID" of a User

        :return: a User model object
        """
        return DaoFactory.getUserDao().get_by_spotify_id(spotifyid)

    @staticmethod
    def create_user(sp: SpotifyHandler):
        user = sp.user_construct_for_creation()

        name = user.display_name
        first_name = name.split()[0]
        if len(name.split()) == 2:
            last_name = name.split()[1]
        else:
            last_name = ""

        DaoFactory.getUserDao().create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=user.id,
                                            email=user.email,
                                            spotify_id=sp.user_token.refresh_token)

    @staticmethod
    def add_new_user_refresh_token(sp: SpotifyHandler):
        _user = sp.user_construct_for_creation()

        user = User.objects.get(username=_user.id)
        user.spotify_id = sp.user_token.refresh_token
        user.save()
