from django.db import models
from events.factory.DAOFactory import DaoFactory


class ParticipationService:

    @staticmethod
    def get_all_by_id(id: int) -> models.QuerySet:
        return DaoFactory.getParticipationDao().get_participation_by_event_id(id)

    @staticmethod
    def user_part_of_event(user_id: int, event_id: int) -> bool:
        """
        Service method used to check whether a specific User has joined an a specific Event

        :param user_id: the primary key "ID" of a User
        :param event_id: the primary key "ID" of an Event

        :return: boolean False if the object is NULL / else True
        """
        if not DaoFactory.getParticipationDao().get_user_in_participation(user_id=user_id, event_id=event_id):
            return False
        return True

    @staticmethod
    def get_all_participation_in_event(event_id: int) -> models.QuerySet:
        """
        Service method used to get all the "participants" of an Event

        :param event_id: the primary key "ID" of an Event

        :return: a set of all the Participation model objects
        """
        return DaoFactory.getParticipationDao().get_participation_in_event(event_id=event_id)