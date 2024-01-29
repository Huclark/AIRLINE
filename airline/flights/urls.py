from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # for every flight to have its own page do this:
    path("<int:flight_id>", views.flight, name="flight"),
    # add a route to book passengers for a flight
    path("<int:flight_id>/book", views.book, name="book")
]
