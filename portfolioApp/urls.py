from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Handles root URL ("/")
    # Keep your other API paths
    path('api/profile/', views.get_profile, name='api-profile'),
    path('api/introduction/', views.IntroductionAPIView.as_view(), name='introduction'),
    path('api/about/', views.AboutSectionAPIView.as_view(), name='api-about'),
    # Add these new Resume endpoints
    path('api/resume/', views.ResumeListCreateAPIView.as_view(), name='resume-list'),
    path('api/resume/<int:pk>/', views.ResumeRetrieveUpdateDestroyAPIView.as_view(), name='resume-detail'),
]