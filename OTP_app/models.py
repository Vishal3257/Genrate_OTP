from django.contrib.auth.models import AbstractUser
from django.db import models
import random
from django.utils import timezone
from datetime import timedelta



# Create your models here.

class User(AbstractUser):
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.otp_created_at = timezone.now()
        self.save()

    def is_otp_valid(self):
        otp_validity_duration = timedelta(minutes=5)
        otp_generation_time = self.otp_created_at  
        return timezone.now() < otp_generation_time + otp_validity_duration
    