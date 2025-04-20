from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('CLIENT', 'Client'),
        ('ADMIN', 'Admin'),
        ('RECEPTIONIST', 'Receptionist'),
        ('TECHNICIAN', 'Technician')
    ]
    fullname = models.CharField(max_length=100 , null=False, blank=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CLIENT')

    def __str__(self):
        return f"{self.username} ({self.role})"