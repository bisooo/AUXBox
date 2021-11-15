from django.db import models
from events.models import participation


class Comment(models.Model):
    """
        Model stores a single User to Event "commenting" relation

        **DESCRIPTION**

        Used to store the User's :model:'events.User' comment in an Event's :model:'events.Event' page
    """
    text = models.CharField(max_length=50, help_text="The user's comment")
    date = models.DateTimeField(auto_now=True, help_text="The date & time of posting the comment")
    participation = models.ForeignKey(participation.Participation, on_delete=models.CASCADE, help_text="The ID for the User's participation in an Event")
