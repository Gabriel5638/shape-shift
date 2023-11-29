from django.db import models
from django.contrib.auth.models import User

class MealJournalEntry(models.Model):
    MEAL_TYPES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snacks', 'Snacks'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    meal = models.TextField() 

    def __str__(self):
        return f"{self.date} - {self.time} - {self.user.username} - {self.meal_type}"
