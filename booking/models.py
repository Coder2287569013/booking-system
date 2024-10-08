from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Room #{self.number}"
    

    class Meta:
        ordering = ["number"]



class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Booking, {self.room}"


    class Meta:
        ordering = ["start_time"]
