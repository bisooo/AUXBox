from time import sleep

from django.test import TestCase

from events.factory.DAOFactory import DaoFactory
from events.models import Event, Invitation
from events.models import User
import copy
import datetime
import time


class BaseTestCase(TestCase):

    def setUp(self) -> None:
        self.event = Event(
            name="Test",
            description="This is a test",
            spotify_genre="xyz",
            location="Prague",
            min_request_price=20,
            date=datetime.date.today(),
            time=datetime.datetime.now().time()
        )
        self.mock_event = DaoFactory.getEventDao().create_event(name="Test",
                                                                description="This is a test",
                                                                spotify_genre="xyz",
                                                                location="Prague",
                                                                min_request_price=20,
                                                                date=datetime.date.today(),
                                                                time=datetime.datetime.now().time())
        self.mock_to_user = DaoFactory.getUserDao().create_user(first_name="Midane Sinana",
                                                                last_name="Nane Nane",
                                                                username="morahazisane",
                                                                email="kamekamekame@siksok.yarrak",
                                                                spotify_id=31)
        self.mock_from_user = DaoFactory.getUserDao().create_user(first_name="Altin Kapilarimiz Kan Oldu Tayfun",
                                                                  last_name="Patatas and Ice Tea",
                                                                  username="karigordumsiktim",
                                                                  email="osmanaga@siksok.yarrak",
                                                                  spotify_id=32)
        self.mock_invitation = DaoFactory.getInvitationDao().create_invitation(self.mock_from_user, self.mock_to_user, self.mock_event)

        self.event2 = DaoFactory.getEventDao().create_event(
            name="Invitation Test",
            description="This is a test",
            spotify_genre="xyz",
            location="Prague",
            min_request_price=20,
            date=datetime.date.today(),
            time=datetime.datetime.now().time()
        )
        self.user = DaoFactory.getUserDao().create_user(
            first_name="Egemen",
            last_name="Erogul",
            username="imam",
            email="imamhaitpler_kapatilsin@gmail.com",
            spotify_id="111QasAssA"
        )

        self.user2 = DaoFactory.getUserDao().create_user(
            first_name="Taysik",
            last_name="Eryarrak",
            username="pic",
            email="imamhaitpler_acilsin@gmail.com",
            spotify_id="AhVAG45AAs"
        )

        self.user3 = DaoFactory.getUserDao().create_user(
            first_name="New",
            last_name="Joiner",
            username="huamina",
            email="kirbacci@gmail.com",
            spotify_id="AdsSsAG45AAs"
        )

        self.invite = DaoFactory.getInvitationDao().create_invitation(
            from_user=self.user,
            to_user=self.user2,
            event=self.event2
        )

        self.participation = DaoFactory.getParticipationDao().create_participation(
            user=self.user3,
            event=self.event2
        )
        
        self.future_event = copy.deepcopy(self.event)
        self.future_event.date = self.event.date + datetime.timedelta(days=1)

        self.old_date_event = copy.deepcopy(self.event)
        self.old_date_event.date = self.event.date - datetime.timedelta(days=1)

        time.sleep(1)
        self.old_time_event = copy.deepcopy(self.event)
