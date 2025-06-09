from django.core.exceptions import ValidationError
from django.db import models

class Introduction(models.Model):
    name = models.CharField(max_length=15, default="Muddassir")
    role = models.CharField(max_length=50, default="MERN Stack Developer")
    experience_years = models.PositiveIntegerField(default=1)  # stored in years now
    projects_completed = models.PositiveIntegerField(default=12)
    countries = models.PositiveIntegerField(default=5)
    short_intro = models.TextField(max_length=100 , default="I turn Figma designs into real web apps using the MERN stack.")
    description = models.TextField(max_length=50 ,default="I love building Websites!")
    

    def __str__(self):
        return f"{self.name} - {self.role}"

    def clean(self):
        if self.experience_years < 0:
            raise ValidationError({'experience_years': 'Experience cannot be negative.'})
