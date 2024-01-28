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
        return f"{self.id}: {self.origin} to {self.destination}"

# create another model for a new table to represent passengers
class Passenger(models.Model):
    # column for first name
    first = models.CharField(max_length=64)
    # column for surname
    last = models.CharField(max_length=64)
    
    # passengers have a many-to-many relationship with flights, for eg:
    # a flight could have multiple passengers or
    # a passenger could be on multiple flights and
    # ultimately we need an additional table to keep track of this
    
    # so we can say that every passenger has flights associated with them which
    # are which are a models.ManyToManyField with Flight
    flights= models.ManyToManyField(Flight, blank=True, related_name="passenger")
    # blank=True caters for the possibility that a passenger has no flight or not been
    # registered for any flights at all
    # related_name is to link Flight to Passenger class
    
    def __str__(self):
        return f"{self.first} {self.last}"
