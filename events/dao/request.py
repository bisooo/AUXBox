from events.dao.base import BaseDao
from django.db import models
from events.models.request import Request
from events.daointerface.requestinterface import RequestDaoInterface


class RequestDao(BaseDao, RequestDaoInterface):

    model = Request
