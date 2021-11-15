from django.db import models
from events.models import event, user, host


class Request(models.Model):
    """
        Model stores a single User in an Event to Host relation for requesting a song
    """
    price = models.PositiveIntegerField(help_text="The price for the song request")
    spotify_song = models.CharField(max_length=50, help_text="The Spotify link of the song requested")
    request_date = models.DateTimeField(auto_now=True, help_text="The date & time when the song was requested")
    state = models.CharField(max_length=50, help_text="The current status of the song request")
    description = models.CharField(max_length=100, help_text="A short description for the song request")
    user = models.ForeignKey(user.User, on_delete=models.CASCADE, help_text="The ID of the User sending the request")
    event = models.ForeignKey(event.Event, on_delete=models.CASCADE, help_text="The ID of the Event where the request was posted")
    host = models.ForeignKey(host.Host, on_delete=models.CASCADE, help_text="the ID of the Host specified for the song request ")
