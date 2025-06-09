from django.contrib import admin
from .models import Profile, Introduction, AboutSection
from .Admin.profile_admin import ProfileAdmin
from .Admin.introduction_admin import IntroductionAdmin
from .Admin.about_admin import AboutSectionAdmin  # Add this line

# Register other models
admin.site.register(Profile, ProfileAdmin)

try:
    admin.site.unregister(Introduction)
except admin.sites.NotRegistered:
    pass
admin.site.register(Introduction, IntroductionAdmin)

# Now register AboutSection properly
try:
    admin.site.unregister(AboutSection)
except admin.sites.NotRegistered:
    pass
admin.site.register(AboutSection, AboutSectionAdmin)
