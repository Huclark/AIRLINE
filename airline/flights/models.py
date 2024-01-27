from django.db import models

# Create your models here.
# Every model is a python class


class Flight(models.Model):
    # populate this model with all the data which will represent the model
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.duration}"
