from django.db import models
from events.models import participation


class Upvote(models.Model):
    """
        Model stores a single User to Event's playlist relation for upvoting songs
    """
    spotify_song = models.CharField(max_length=50, help_text="The Spotify song to be upvoted")
    date = models.DateTimeField(auto_now=True, help_text="The date & time of the upvoting")
    participation = models.ForeignKey(participation.Participation, on_delete=models.CASCADE, help_text="The Participation ID of the User in that Event ")
