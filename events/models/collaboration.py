from django.db import models
from events.models import event, host


class Collaboration(models.Model):
    """
        Model stores a single Host to Event relation

        **DESCRIPTION**

        Used to store the multiple Hosts :model:'events.Host' that are part of the same Event :model:'events.Event' with their set times & playlists
    """
    start_set_time = models.DateTimeField(help_text="The starting time of a DJ's set")
    end_set_time = models.DateTimeField(help_text="The ending time of a DJ's set")
    host = models.ForeignKey(host.Host, on_delete=models.CASCADE, help_text="The Host's ID as a foreign key")
    event = models.ForeignKey(event.Event, on_delete=models.CASCADE, help_text="The Event's ID as a foreign key")
    spotify_playlist = models.CharField(max_length=50, help_text="The link to the DJ's set Spotify playlist")

    class Meta:
        unique_together = ('host', 'event',)
