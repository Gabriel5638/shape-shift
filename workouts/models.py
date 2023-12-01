from django.db import models
from django.contrib.auth.models import User


class WorkoutTracker(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    title = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=15, choices=DAY_CHOICES)  # Use choices here
    duration = models.IntegerField(help_text="Duration in minutes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.get_day_of_week_display()}"
