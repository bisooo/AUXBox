from django.db import models
from events.daointerface.baseinterface import BaseDaoInterface


class BaseDao(BaseDaoInterface):
    """
    Abstract Base class for the DAO
    """

    model = models.Model

    @staticmethod
    def save(obj):
        """
        DAO method creates an instance of the passed model object in the database

        :param obj: a model object

        :return: a model object
        """
        if obj:
            return obj.save()


    @staticmethod
    def delete(obj):
        """
        DAO method removes the passed model object instance from the database

        :param obj: a model object

        :return: a model object
        """
        if obj:
            obj.delete()


    def all(self):
        """
        DAO method queries the database for all the instances of a specific model

        :return: a set of all the model objects
        """
        return self.model.objects.all()