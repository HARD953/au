from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class DonneeCollecteeListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer

class DonneeCollecteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer

class SupportPublicitaireListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer

class SupportPublicitaireDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer