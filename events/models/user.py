from django.db import models


class User(models.Model):
    """
        Model stores a single User entity
    """
    first_name = models.CharField(max_length=50, help_text="The first name of the User")
    last_name = models.CharField(max_length=50, help_text="The last name of the User")
    username = models.CharField(max_length=50, unique=True, help_text="The username of the User")
    email = models.EmailField(unique=True, help_text="The email address of the User")
    spotify_id = models.CharField(max_length=250, help_text="The unique Spotify ID of the User")

    # "getters" for certain fields of a User
    def __str__(self):
        return self.first_name + ' ' + self.last_name