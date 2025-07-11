from django.db import models
from django.core.exceptions import ValidationError

class Service(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="e.g., Frontend Developer"
    )
    description = models.TextField(
        help_text="Describe what the service includes"
    )
    projects = models.PositiveIntegerField(
        help_text="Number of completed projects"
    )

    def clean(self):
        # Ensure projects is not None and non-negative
        if self.projects is not None and self.projects < 0:
            raise ValidationError("Projects must be a positive number.")

    def __str__(self):
        return self.title
