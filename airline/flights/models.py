from django.db import models

# Create your models here.
# Every model is a python class

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # populate this model with all the data which will represent the model
    # origin = models.CharField(max_length=64) => this was before Airport class
    # we need to link the Airport table to the Flight table by using a foreign key
    # CASCADE makes sure that a flight whose airport has been deleted from the 
    # table will also be deleted in the flight table
    # departures is the name given to link the airport
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.duration}"
