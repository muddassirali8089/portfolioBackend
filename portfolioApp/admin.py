from django.contrib import admin
from .models import Profile, Introduction, AboutSection, Resume

# Import all Admin classes
from .Admin.profile_admin import ProfileAdmin
from .Admin.introduction_admin import IntroductionAdmin
from .Admin.about_admin import AboutSectionAdmin
from .Admin.resume_admin import ResumeAdmin

# First unregister any previously registered models
try:
    admin.site.unregister(Introduction)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(AboutSection)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Profile)
except admin.sites.NotRegistered:
    pass

try:
    admin.site.unregister(Resume)
except admin.sites.NotRegistered:
    pass

# Then register fresh with custom Admin classes
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(Resume, ResumeAdmin)