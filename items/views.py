from rest_framework import generics
from .models import SpecificItem, VagueItem
from .serializers import SpecificItemSerializer, VagueItemSerializer

class SpecificEntryView(generics.ListCreateAPIView):
    queryset = SpecificItem.objects.all()
    serializer_class = SpecificItemSerializer

class VagueEntryView(generics.ListCreateAPIView):
    queryset = VagueItem.objects.all()
    serializer_class = VagueItemSerializer
