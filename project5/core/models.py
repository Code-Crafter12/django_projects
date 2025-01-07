from django.db import models
import os


# Create your models here.
class ServiceBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    service_date = models.DateField()
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
    
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')