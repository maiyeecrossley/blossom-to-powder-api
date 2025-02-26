from django.db import models

SEASONS = [
    ("Spring", "Spring 🌸"),
    ("Summer", "Summer ☀️"),
    ("Autumn", "Autumn 🍂"),
    ("Winter", "Winter ❄️"),
]

MONTHS = [
    ("Jan", "January"),
    ("Feb", "Febraury"),
    ("Mar", "March"),
    ("Apr", "April"),
    ("May", "May"),
    ("Jun", "June"),
    ("Jul", "July"),
    ("Aug", "August"),
    ("Sep", "September"),
    ("Oct", "October"),
    ("Nov", "November"),
    ("Dec", "December"),
]

# Create your models here.

class Seasons(models.Model):
    name = models.CharField(choices=SEASONS)
    description = models.TextField(max_length=500)
    month_from = models.CharField(choices=MONTHS)
    month_to = models.CharField(choices=MONTHS)

    def __str__(self):
        return f'{self.name}: {self.month_from} - {self.month_to}'
