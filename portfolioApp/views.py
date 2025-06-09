from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

# Function-based view (for specific custom endpoints)
@api_view(['GET'])
def get_profile(request):
    """
    Function-based API endpoint to get profile data
    """
    profile = Profile.objects.first()
    
    if not profile:
        return Response(
            {"error": "Profile not found"}, 
            status=404
        )
    
    serializer = ProfileSerializer(profile, context={'request': request})
    return Response(serializer.data)
