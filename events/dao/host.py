from django.db import models
from events.models.host import Host
from events.daointerface.hostinterface import HostDaoInterface
from events.dao.base import BaseDao


class HostDao(BaseDao, HostDaoInterface):

    model = Host
