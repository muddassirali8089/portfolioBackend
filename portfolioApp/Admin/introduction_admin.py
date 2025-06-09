from django.contrib import admin
from ..models import Introduction

@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'experience_years', 'projects_completed', 'countries')

    # Removed search bar by not including search_fields

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'role'),
        }),
        ('Stats', {
            'fields': ('experience_years', 'projects_completed', 'countries'),
        }),
        ('Intro & Description', {
            'fields': ('short_intro', 'description'),
        }),
    )

    # Only allow editing one instance
    def has_add_permission(self, request):
        return not Introduction.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
