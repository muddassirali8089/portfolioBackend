# Import admin site
from django.contrib import admin

# Import models
from .models import Profile, Introduction, AboutSection, Education, Experience , Service , Skill

# Import custom admin classes from separate files
from .Admin.profile_admin import ProfileAdmin
from .Admin.introduction_admin import IntroductionAdmin
from .Admin.about_admin import AboutSectionAdmin
from .Admin.resume import EducationAdmin, ExperienceAdmin 
from .Admin.service_admin import ServiceAdmin

from .Admin.skill_admin import SkillAdmin




# Unregister existing models to avoid duplicate registration errors
for model in [Profile, Introduction, AboutSection, Education, Experience , Skill]:
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass

# Register each model with its custom admin class
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)
