from events.daointerface.baseinterface import BaseDaoInterface
from events.models.participation import Participation
from django.db import models


class ParticipationDaoInterface(BaseDaoInterface):

    model = Participation

    def get_participation_by_event_id(self, id: int) -> models.QuerySet:
        """ query database for a participation by event id """
        pass

    def get_user_in_participation(self, user_id: int, event_id: int) -> Participation:
        """ query the database for a user in a participation """
        pass

    def get_participation_in_event(self, event_id: int) -> models.QuerySet:
        """ query the database for the participations in an event """
        pass