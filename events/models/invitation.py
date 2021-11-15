from django.db import models
from events.models import participation
from events.models import user
from events.models import event


class Invitation(models.Model):
    """
        Models stores a single invitation relation between 2 Users

        **DESCRIPTION**

        Used to store the IDs of the inviting and invited Users :model:'events.User' aswell as the date & time of the invitation
    """
    created_on = models.DateTimeField(auto_now=True, help_text="The data & time of the invitation")
    from_user = models.ForeignKey(user.User, on_delete=models.CASCADE,
                                  help_text="The ID of the User that sent the invitation", related_name="from_user")
    to_user = models.ForeignKey(user.User, on_delete=models.CASCADE, help_text="The ID of the User invited")
    event = models.ForeignKey(event.Event, on_delete=models.CASCADE, related_name="event",null="true")
    state = models.PositiveSmallIntegerField(
        choices=(
            (0, 'Rejected'),
            (1, 'Accepted'),
            (2, 'Pending'),
        ))

    class Meta:
        unique_together = ('from_user', 'to_user',)
