from django.contrib import admin
from .models import Profile, Introduction, AboutSection, Education, Experience

# Import custom admin classes
from .Admin.profile_admin import ProfileAdmin
from .Admin.introduction_admin import IntroductionAdmin
from .Admin.about_admin import AboutSectionAdmin
from .Admin.resume import EducationAdmin, ExperienceAdmin  # ✅ Moved here

# Unregister to avoid duplicate registration errors (safe cleanup)
for model in [Profile, Introduction, AboutSection, Education, Experience]:
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass

# Register models with their custom admin classes
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
