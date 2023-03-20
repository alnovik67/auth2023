from django.db import models
from django.shortcuts import reverse


# Create your models here.
class User1page(models.Model):
    """
    Model representing a User1 Data.
    """
    name = models.CharField(max_length=200, help_text="Enter User1 data.")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('User1page')


class User2page(models.Model):
    """
    Model representing a User2 Data.
    """
    name = models.CharField(max_length=200, help_text="Enter User2 data.")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('User2page')
