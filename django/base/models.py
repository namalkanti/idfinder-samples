from django.db import models
from django.conf import settings

DEFAULT_MAX_LENGTH = 200
ID_CARD_LENGTH = 7

class CardData(models.Model):
    """
    Model for storing card information.
    """
    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    id_number = models.CharField(max_length=ID_CARD_LENGTH)
    picture = models.ImageField(upload_to="")
    email = models.EmailField()
    passphrase = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    active = models.BooleanField(default=True)

    def not_found(self):
        """
        Determines if the id card has been found or not.
        """
        return self.active

    def mark_found(self, given_phrase):
        """
        Marks id card as found in the database.
        """
        if self.passphrase == given_phrase:
            self.active = False
            self.save()
            return True
        return False
