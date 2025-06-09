# your_app/admin/profile_admin.py
from django.contrib import admin
from django.utils.html import format_html
from ..models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'address', 'whatsapp_link', 'linkedin_link',
        'instagram_link', 'github_link', 'logo_image', 'picture_image'
    )

    def logo_image(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.logo.url)
        return "No Logo"
    logo_image.short_description = 'Logo'

    def picture_image(self, obj):
        if obj.picture:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.picture.url)
        return "No Picture"
    picture_image.short_description = 'Picture'

    def has_add_permission(self, request):
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
