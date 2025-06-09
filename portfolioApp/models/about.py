from django.db import models
from django.core.exceptions import ValidationError

class AboutSection(models.Model):
    title_line_1 = models.CharField(max_length=50, help_text="First line of heading", default="Every great project begins with")
    title_line_2 = models.CharField(max_length=50, help_text="Second line with highlighted word", default="a passion for")
    title_highlight = models.CharField(max_length=10, default="coding")
    paragraph = models.TextField(max_length=500, help_text="Main about paragraph")

    def clean(self):
        if len(self.paragraph.strip()) == 0:
            raise ValidationError({"paragraph": "Paragraph cannot be empty."})

        if len(self.title_highlight.strip()) > 10:
            raise ValidationError({"title_highlight": "Highlight text cannot be longer than 10 characters."})

        # Remove this check to allow title_highlight to be rendered separately
        # If you still want to keep a soft check, do it with a warning in the admin, not a hard error

    def __str__(self):
        return "About Section"

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"
