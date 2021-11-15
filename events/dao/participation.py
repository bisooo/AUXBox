from events.dao.base import BaseDao
from events.models.participation import Participation
from events.models.event import Event
from django.db import models
from events.daointerface.participationinterface import ParticipationDaoInterface


class ParticipationDao(BaseDao, ParticipationDaoInterface):
    model = Participation

    def get_participation_by_event_id(self, id: int) -> models.QuerySet:
        """
        DAO method used to query the database for all the participants of the specified Event "ID"

        :param event_id: the primary key "ID" of an Event

        :return: a set of all the Participation model objects
        """
        return self.model.objects.filter(event_id=id).all()

    def get_user_in_participation(self, user_id: int, event_id: int) -> Participation:
        """
        DAO method used to query the database for a "participation" of a User in an Event by their IDs

        :param user_id: the primary key "ID" of a User
        :param event_id: the primary key "ID" of an Event

        :return: a Participation model object
        """
        return self.model.objects.filter(event_id=event_id, user_id=user_id)

    def get_participation_in_event(self, event_id: int) -> models.QuerySet:
        return self.model.objects.filter(event_id=event_id)

    def check_participation (self, event_id: int, user_id: int):
        return self.model.objects.filter(event_id=event_id, user_id=user_id).exists()

    def create_participation (self, user, event):
        return self.model.objects.create(user=user, event=event)
