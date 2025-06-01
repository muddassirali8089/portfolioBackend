from django.contrib import admin
from .models import Profile
from django.utils.html import format_html

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

    # ✅ Prevent adding more than one profile
    def has_add_permission(self, request):
        # If there's already one profile, don't allow adding more
        if Profile.objects.exists():
            return False
        return True

    # ✅ Optional: Prevent deleting profile from admin (to avoid frontend issues)
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Profile, ProfileAdmin)
