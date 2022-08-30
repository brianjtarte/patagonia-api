from rest_framework import generics
from .serializer import CampsiteSerializer
from .models import Campsite

class CampsiteList(generics.ListAPIView):
    queryset = Campsite.objects.all()
    serializer_class = CampsiteSerializer

class CampsiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campsite.objects.all()
    serializer_class = CampsiteSerializer

# Create your views here.
