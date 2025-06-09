from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Introduction
from .serializers import IntroductionSerializer
from .models import AboutSection
from .serializers import AboutSectionSerializer

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


class IntroductionAPIView(APIView):
    def get(self, request):
        intro = Introduction.objects.first()  # assuming only one record
        serializer = IntroductionSerializer(intro)
        return Response(serializer.data)


class AboutSectionAPIView(APIView):
    def get(self, request):
        about = AboutSection.objects.first()  # Assuming only one row
        serializer = AboutSectionSerializer(about)
        return Response(serializer.data)