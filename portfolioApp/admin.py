from django.contrib import admin
from .models import Profile, Introduction
from .Admin.profile_admin import ProfileAdmin
from .Admin.introduction_admin import IntroductionAdmin

admin.site.register(Profile, ProfileAdmin)

# Unregister if already registered, then register your admin
try:
    admin.site.unregister(Introduction)
except admin.sites.NotRegistered:
    pass

admin.site.register(Introduction, IntroductionAdmin)
