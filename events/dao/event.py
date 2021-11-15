from events.dao.base import BaseDao
from django.db import models
from events.models.event import Event
from django.utils import timezone
import datetime
from events.daointerface.eventinterface import EventDaoInterface


class EventDao(BaseDao, EventDaoInterface):
    model = Event

    def find_by_id(self, id: int) -> Event:
        """
        DAO method used to query the database for an Event by its "ID"

        :param id: the primary key "ID" of an Event

        :return: an Event model object
        """
        return self.model.objects.all().filter(id=id).get()

    def find_all_upcoming(self) -> models.QuerySet:
        """
        DAO method used to query the database for all the events that are in the coming days

        :return: a set of all the Event model objects
        """
        today = timezone.now()
        return self.model.objects.all().filter(date__gte=today)

    def create_event(self, name: str, description: str, spotify_genre: str
                     , location: str, min_request_price: int
                     , date: datetime.date, time: datetime.time) -> Event:
        """
        DAO method used to create an instance in the database of the Event model from the passed validated argument fields

        :param name: Name of the Event
        :param description: Description of the Event
        :param spotify_genre: Spotify Genre of the Event
        :param location: Location of the Event
        :param min_request_price: Minimum song request price
        :param date: Date of the Event
        :param time: Time of the Event

        :return: an Event model object
        """
        return self.model.objects.create(name=name,
                                         description=description,
                                         spotify_genre=spotify_genre,
                                         location=location,
                                         min_request_price=min_request_price,
                                         date=date,
                                         time=time)
