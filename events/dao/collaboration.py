from django.db import models
from events.models.collaboration import Collaboration
from events.daointerface.collaborationinterface import CollaborationDaoInterface
from events.dao.base import BaseDao


class CollaborationDao(BaseDao, CollaborationDaoInterface):

    model = Collaboration
