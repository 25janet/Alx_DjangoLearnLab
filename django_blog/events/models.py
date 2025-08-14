from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hosted_events")
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class EventRSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="rsvps")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_status = models.CharField(
        max_length=20,
        choices=[('going', 'Going'), ('interested', 'Interested'), ('not_going', 'Not Going')]
    )
    responded_at = models.DateTimeField(auto_now_add=True)
#remember class meta is class within a class that defines gow the class behaves
    class Meta:
        unique_together = ('event', 'user')
#the unique_together rule means that certain fields in your model must always be unique when combined. In the above i have two fields: event and user.
#So, in simple terms, unique_together = ('event', 'user') makes sure that each user can only sign up for each event one time.
    def __str__(self):
        return f"{self.user.username} RSVP'd {self.rsvp_status} to {self.event.name}"

