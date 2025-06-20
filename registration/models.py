from django.db import models
from django.conf import settings
from events.models import Event

class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('registered', 'Registered'),
        ('not_registered', 'Not Registered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')

    def __str__(self):
        return f"{self.name} ({self.user.username}) - {self.event}"
