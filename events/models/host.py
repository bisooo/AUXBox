from django.db import models
from events.models import user


class Host(models.Model):
    """
        Model stores a single Host entity entry
    """
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
