from django.contrib import admin
from ..models import Resume  # Make sure this import path is correct

@admin.register(Resume)  # ← Add the model here
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'company')
    search_fields = ('title', 'company')
    ordering = ('-date',)  # Newest first