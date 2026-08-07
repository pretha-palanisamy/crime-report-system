from django.db import models
from django.contrib.auth.models import User

class Crime(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Under Investigation', 'Under Investigation'),
        ('Solved', 'Solved'),
    ]

    CRIME_TYPES = [
        ('Theft', 'Theft'),
        ('Assault', 'Assault'),
        ('Fraud', 'Fraud'),
        ('Cyber Crime', 'Cyber Crime'),
        ('Other', 'Other'),
    ]

    crime_type = models.CharField(max_length=50, choices=CRIME_TYPES)
    location = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    date_reported = models.DateTimeField(auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='crimes_reported')
    photo=models.ImageField(upload_to='crime+photos/',blank=True,null=True)

    def __str__(self):
        return f"{self.crime_type} - {self.location}"