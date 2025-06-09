from django.urls import path
from . import views  # Import the whole views module

urlpatterns = [
    path('api/profile/', views.get_profile, name='api-profile'),  # Use it from the module
]
