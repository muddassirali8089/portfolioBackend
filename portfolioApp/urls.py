from django.urls import path
from . import views  # Import the whole views module

urlpatterns = [
    path('api/profile/', views.get_profile, name='api-profile'),
    path('api/introduction/', views.IntroductionAPIView.as_view(), name='introduction'),  # Add views. prefix
    path('api/about/', views.AboutSectionAPIView.as_view(), name='api-about'),
]
