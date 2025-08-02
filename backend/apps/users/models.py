from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    wallet_address = models.CharField(max_length=255, blank=True, null=True)
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('creator', 'Creator'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')

    def __str__(self):