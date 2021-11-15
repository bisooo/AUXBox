from events.dao.base import BaseDao
from django.db import models
from events.models import Friendship
from django.utils import timezone
import datetime
from events.daointerface.eventinterface import EventDaoInterface
from django.db.models import Q


class FriendshipDao:
    model = Friendship

    def get_friendships(self):
        return self.model.objects.all()

    def get_accepted_friendships(self, user):
        return self.model.objects.filter(Q(state=1, requester=user) | Q(state=1, receiver=user))

    def get_rejected_friendships(self, user):
        return self.model.objects.filter(Q(state=0, requester=user) | Q(state=0, receiver=user))

    def filter_users(self, user, query :str):
        return self.model.objects.filter(
            (Q(receiver=user)
            & (Q(requester__first_name__icontains=query) | Q(requester__last_name__icontains=query)
            | Q(requester__username__icontains=query) | Q(requester__email__icontains=query)) )
            | (Q(requester=user)
            & (Q(receiver__first_name__icontains=query) | Q(receiver__last_name__icontains=query)
            | Q(receiver__username__icontains=query) | Q(receiver__email__icontains=query)) )
        )
