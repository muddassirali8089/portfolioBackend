from django.contrib import admin
from ..models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'projects')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'projects')
        }),
    )

