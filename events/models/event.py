from django.db import models
from django.urls import reverse
from django.utils import timezone


class Event( models.Model ) :
    """
        Model stores a single Event entity entry
    """
    name = models.CharField(max_length=50, help_text="The Event's name")
    description = models.CharField(max_length=100, help_text="A short Event description")
    spotify_genre = models.CharField(max_length=50, help_text="The Event's Genre")
    location = models.CharField(max_length=50, help_text="The Event's location")
    min_request_price = models.PositiveIntegerField(help_text="The minimum price per song request")
    date = models.DateField(help_text="The Date of the Event")
    time = models.TimeField(default=timezone.now, help_text="The Time of the Event")

    class Meta:
        unique_together = ()

    # "getters" for certain fields of an Event
    def get_absolute_url(self):
        return reverse('view_event', args=[self.id])

    def __str__(self):
        return self.name + ' ' + self.description + ' ' + self.spotify_genre + ' ' + self.location