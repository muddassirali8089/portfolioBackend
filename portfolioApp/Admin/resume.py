from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from portfolioApp.models.resume import Education
from portfolioApp.models.resume import Experience, MONTH_CHOICES, YEAR_CHOICES


# -------- Education Admin --------
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'university_name', 'start_year', 'end_year')
    fields = ('title', 'university_name', 'start_year', 'end_year')


# -------- Experience Admin with Conditional End Date Logic --------
class ExperienceAdminForm(forms.ModelForm):
    end_month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)
    end_year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)

    class Meta:
        model = Experience
        fields = '__all__'

    class Media:
        js = ('admin/js/experience_admin.js',)  # optional JS to toggle end fields


class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceAdminForm
    list_display = ('title', 'company_name', 'start_month', 'start_year', 'end_month', 'end_year', 'is_present')
    fields = ('title', 'company_name', 'start_month', 'start_year', 'is_present', 'end_month', 'end_year')


# -------- Register both models --------

