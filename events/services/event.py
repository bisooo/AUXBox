import datetime
from events.dao.event import EventDao
from events.dao.base import BaseDao
from django.db.models import QuerySet
from django.core.exceptions import ValidationError
from events.factory.DAOFactory import DaoFactory


class EventService:

    @staticmethod
    def get_event_by_id(id: int) -> EventDao.model:
        """
        Service method used to get an Event by its "ID"

        :param id: the primary key "ID" of an Event

        :return: an Event model object
        """
        return DaoFactory.getEventDao().find_by_id(id)


    @staticmethod
    def get_upcoming_events() -> QuerySet:
        """
        Service method used to get a list of all events that are upcoming

        :return: a set of all the Event model objects
        """
        return DaoFactory.getEventDao().find_all_upcoming()


    @staticmethod
    def create_event_from_form(event):
        """
        Service method used to validate the date & time specified before creating an Event

        :param event: the Event model object

        :return: an Event model object
        """
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()

        if event.date < current_date:
            raise ValidationError('date cannot be in the past')
        if event.date == current_date and event.time < current_time:
            raise ValidationError('time cannot be in the past')

        event = DaoFactory.getEventDao().create_event(name=event.name,
                                                      description=event.description,
                                                      spotify_genre=event.spotify_genre,
                                                      location=event.location,
                                                      min_request_price=int(event.min_request_price),
                                                      date=event.date,
                                                      time=event.time)
        return event