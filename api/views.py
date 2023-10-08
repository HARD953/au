from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class DonneeCollecteeListCreateView(generics.ListCreateAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer

class DonneeCollecteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer

class SupportPublicitaireListView(generics.ListCreateAPIView):
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer

class SupportPublicitaireDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer