from django.db import models

SEASONS = [
    ("Spring", "Spring 🌸"),
    ("Summer", "Summer ☀️"),
    ("Autumn", "Autumn 🍂"),
    ("Winter", "Winter ❄️"),
]

MONTHS = [
    ("01", "January"),
    ("02", "February"),
    ("03", "March"),
    ("04", "April"),
    ("05", "May"),
    ("06", "June"),
    ("07", "July"),
    ("08", "August"),
    ("09", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December"),
]

# Create your models here.

class Seasons(models.Model):
    name = models.CharField(choices=SEASONS)
    description = models.TextField(max_length=500, null=True, blank=True)
    start_month = models.CharField(null=True, blank=True, choices=MONTHS)
    end_month = models.CharField(null=True, blank=True, choices=MONTHS)

    def __str__(self):
        return f'{self.name}: {self.start_month} - {self.end_month}'

    @classmethod
    def get_valid_months(cls):
        return [month[0] for month in cls._meta.get_field('start_month').choices]

    def get_all_months(self):
        month_list = Seasons.get_valid_months()

        if self.start_month not in month_list or self.end_month not in month_list:
            raise ValueError(f"Invalid start or end month: {self.start_month}, {self.end_month}")

        start_idx = month_list.index(self.start_month)
        end_idx = month_list.index(self.end_month)

        return month_list[start_idx:end_idx + 1] if start_idx <= end_idx else month_list[start_idx:] + month_list[:end_idx + 1]