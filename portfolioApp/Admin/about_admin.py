from django.contrib import admin
from ..models import AboutSection

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title_highlight',)  # Removed 'subtitle'

    fieldsets = (
        ("Heading Info", {
            'fields': ('title_line_1', 'title_line_2', 'title_highlight'),  # Removed 'subtitle'
        }),
        ("About Description", {
            'fields': ('paragraph',),
        }),
    )

    def has_add_permission(self, request):
        # Only allow one About section
        return not AboutSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
