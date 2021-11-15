from django.db import models
from .user import User


class Friendship(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requester")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    state = models.PositiveSmallIntegerField(
        choices=(
            (0, 'Rejected'),
            (1, 'Accepted'),
            (2, 'Pending'),
        ))

    class Meta:
        unique_together = ("requester", "receiver",)
