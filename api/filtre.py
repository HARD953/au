from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from custumer.models import*
from custumer.serializers import UserSerializer1
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import *
from datetime import datetime
from .serializers2 import *

class SupportPublicitaireListViewF(generics.ListCreateAPIView):
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializerF


class MarqueListViewF(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializerF

class VisibiliteListViewF(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Visibilite.objects.all()
    serializer_class = VisibiliteSerializerF

class EtatListViewF(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Etat.objects.all()
    serializer_class = EtatSerializerF

class CanalListViewF(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Canal.objects.all()
    serializer_class = CanalSerializerF

class SiteListViewF(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Site.objects.all()
    serializer_class = SiteSerializerF

class QuartierListViewF(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = DonneeCollectee.objects.all()
    serializer_class = FiltreQuartier



