from django.db import models

class Resume(models.Model):
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-date']  # Newest first

    def __str__(self):
        return f"{self.title} at {self.company}"