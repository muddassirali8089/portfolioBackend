from django.contrib import admin
from portfolioApp.models import Education, Experience

class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'university_name', 'start_year', 'end_year')
    fields = ('title', 'university_name', 'start_year', 'end_year')

from django.contrib import admin
from portfolioApp.models import Experience
from django.utils.safestring import mark_safe

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'start_month', 'start_year', 'end_month', 'end_year', 'is_present')
    fields = ('title', 'company_name', 'start_month', 'start_year', 'is_present', 'end_month', 'end_year')





