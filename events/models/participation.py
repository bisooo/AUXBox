from django.db import models
from events.models import event, user


class Participation(models.Model):
    """
        Model stores a single User to Event relation

        **DESCRIPTION**

        Used to store the Event IDs & the User IDs :model:'events.User' that they are going to that Event :model:'events.Event'
    """
    user = models.ForeignKey(user.User, on_delete=models.CASCADE, help_text="The ID of the User")
    event = models.ForeignKey(event.Event, on_delete=models.CASCADE, help_text="The ID of the Event")

    class Meta:
        unique_together = ('user', 'event',)
