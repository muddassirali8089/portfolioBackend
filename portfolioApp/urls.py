# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),  # Handles root URL ("/")
#     # Keep your other API paths
#     path('api/profile/', views.get_profile, name='api-profile'),
#     path('api/introduction/', views.IntroductionAPIView.as_view(), name='introduction'),
#     path('api/about/', views.AboutSectionAPIView.as_view(), name='api-about'),
#     # Add these new Resume endpoints
#     path('api/resume/', views.ResumeEntryListCreateAPIView.as_view(), name='resume-list'),

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Handles root URL ("/")
    path('api/profile/', views.get_profile, name='profile'),
    path('api/introduction/', views.IntroductionAPIView.as_view(), name='introduction'),
    path('api/about/', views.AboutSectionAPIView.as_view(), name='about'),

    # ✅ Education
    path('api/education/', views.EducationListCreateAPIView.as_view(), name='education-list'),
    path('api/education/<int:pk>/', views.EducationDetailAPIView.as_view(), name='education-detail'),

    path('education/', views.EducationListView.as_view(), name='education-list'),
    path('experience/', views.ExperienceListView.as_view(), name='experience-list'),
]
