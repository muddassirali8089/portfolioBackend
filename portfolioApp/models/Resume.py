from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

# Helpers
MONTH_CHOICES = [
    ("01", "January"), ("02", "February"), ("03", "March"), ("04", "April"),
    ("05", "May"), ("06", "June"), ("07", "July"), ("08", "August"),
    ("09", "September"), ("10", "October"), ("11", "November"), ("12", "December"),
]

YEAR_CHOICES = [(str(r), str(r)) for r in range(1980, datetime.now().year + 10)]
YEAR_CHOICES_WITH_PRESENT = [("Present", "Present")] + YEAR_CHOICES

# =============================
# ✅ Education Model
# =============================
class Education(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., 'BS Software Engineering'")
    university_name = models.CharField(max_length=200, default="Not specified", help_text="e.g., 'COMSATS University'")

    start_year = models.CharField(max_length=4, choices=YEAR_CHOICES, default=str(datetime.now().year))
    end_year = models.CharField(
        max_length=10,
        choices=YEAR_CHOICES_WITH_PRESENT,
        default="Present",
        help_text="Select end year or 'Present'"
    )

    def clean(self):
        if self.end_year != "Present" and int(self.start_year) > int(self.end_year):
            raise ValidationError("Start year must be before or equal to end year.")

    def __str__(self):
        return f"{self.title} at {self.university_name} ({self.start_year} - {self.end_year})"

# =============================
# ✅ Experience Model
# =============================
class Experience(models.Model):
    title = models.CharField(max_length=200, help_text="e.g., 'Frontend Developer'")
    company_name = models.CharField(max_length=200, default="Not specified", help_text="e.g., 'Codematics Inc or GIKI IT Center Islamabad'")

    start_month = models.CharField(max_length=2, choices=MONTH_CHOICES, default="01")
    start_year = models.CharField(max_length=4, choices=YEAR_CHOICES, default=str(datetime.now().year))

    end_month = models.CharField(
    max_length=2,
    choices=MONTH_CHOICES,
    blank=True,
    null=True
    )   

    end_year = models.CharField(
    max_length=4,
    choices=YEAR_CHOICES,
    blank=True,
    null=True
    )

    is_present = models.BooleanField(default=False, help_text="Check if currently working here")

    def clean(self):
        if self.is_present:
            if self.end_month or self.end_year:
                raise ValidationError("You selected 'Present' but also provided an end date.")
            # ✅ Set them to None explicitly just in case
            self.end_month = None
            self.end_year = None
        else:
            if not self.end_month or not self.end_year:
                raise ValidationError("Please provide both end month and year or mark as Present.")
            if int(self.start_year) > int(self.end_year):
                raise ValidationError("Start year must be before or equal to end year.")
            if self.start_year == self.end_year and self.start_month > self.end_month:
                raise ValidationError("Start month must be before end month in the same year.")

    def __str__(self):
        if self.is_present:
            return f"{self.title} at {self.company_name} ({self.start_month}/{self.start_year} - Present)"
        return f"{self.title} at {self.company_name} ({self.start_month}/{self.start_year} - {self.end_month}/{self.end_year})"
