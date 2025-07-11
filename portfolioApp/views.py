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
from django.shortcuts import render
from rest_framework import generics
from .models import Education, Experience
from .serializers import EducationSerializer, ExperienceSerializer
from .models import Service
from .serializers import ServiceSerializer


# Function-based view (for specific custom endpoints)



def home(request):
    return render(request, 'portfolioApp/home.html')
  

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
    


from .models import Education, Experience
from .serializers import EducationSerializer, ExperienceSerializer
from rest_framework import generics


# For Education
class EducationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class EducationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

from rest_framework import generics
from .models import Education, Experience
from .serializers import EducationSerializer, ExperienceSerializer

class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all().order_by('-start_year')
    serializer_class = EducationSerializer

class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all().order_by('-start_year')
    serializer_class = ExperienceSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ServiceListAPIView(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

