from django.db import models
from events.daointerface.baseinterface import BaseDaoInterface
from events.models.event import Event
from django.utils import timezone
import datetime


class EventDaoInterface(BaseDaoInterface):

    model = Event

    def find_by_id(self, id: int) -> model:
        """ query database for an event by id """
        pass

    def find_all_upcoming(self) -> models.QuerySet:
        """ query for all upcoming events """
        pass

    def create_event(self, name: str, description: str, spotify_genre: str
                     , location: str, min_request_price: int
                     , date: datetime.date, time: datetime.time) -> models.QuerySet:
        """ create an event instance with the given parameters """
        pass
