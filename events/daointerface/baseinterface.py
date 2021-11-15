from django.db import models


class BaseDaoInterface:

    model = models.Model

    @staticmethod
    def save(obj):
        """ save obj to database """
        pass

    @staticmethod
    def delete(obj):
        """ delete obj from database """
        pass

    def all(self):
        """ get all instances from the database"""
        pass
