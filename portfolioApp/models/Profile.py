from django.db import models
from django.core.validators import MaxLengthValidator

class Profile(models.Model):
    logo = models.ImageField(upload_to='logos/', null=True)       # for image upload
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True) # for image upload
    email = models.EmailField()
    address = models.CharField(
        max_length=20,
        validators=[MaxLengthValidator(20)]
    )
    whatsapp_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'Profile'
