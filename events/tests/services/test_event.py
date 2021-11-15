from events.tests import BaseTestCase
from events.services.event import EventService
from django.core.exceptions import ValidationError
from events.dao.event import EventDao

class EventTestCase(BaseTestCase):

    def test_events_in_future_are_added_to_db(self):
        entries = EventDao().find_all_upcoming().count()
        EventService().create_event_from_form(self.future_event)

        new_entries = EventDao().find_all_upcoming().count()
        self.assertEquals(new_entries, entries + 1)

    def test_events_in_the_past_cannot_be_added_to_db(self):

        with self.assertRaisesMessage(ValidationError, 'date cannot be in the past'):
            EventService().create_event_from_form(self.old_date_event)

        with self.assertRaisesMessage(ValidationError, 'time cannot be in the past'):
            EventService().create_event_from_form(self.old_time_event)
