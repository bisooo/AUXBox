from events.dao.base import BaseDao
from django.db import models
from events.models.upvote import Upvote
from events.daointerface.upvoteinterface import UpvoteDaoInterface


class UpvoteDao(BaseDao, UpvoteDaoInterface):

    model = Upvote
