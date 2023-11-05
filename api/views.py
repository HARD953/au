from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class DonneeCollecteeCreateView(generics.CreateAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer
    def perform_create(self, serializer):
        # Associer l'utilisateur connecté comme propriétaire du Bien
        if self.request.user.is_anonymous:
            serializer.save()
        else:
            serializer.save(agent=self.request.user)

class DonneeCollecteeListView(generics.ListAPIView):
    serializer_class = DonneeCollecteeSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filtrer les objets Bien pour l'utilisateur connecté
            return DonneeCollectee.objects.filter(agent=self.request.user)
        else:
            # Renvoyer tous les objets Bien si personne n'est connecté
            return DonneeCollectee.objects.all()
       
class DonneeCollecteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonneeCollecteeSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filtrer les objets Bien pour l'utilisateur connecté
            return DonneeCollectee.objects.filter(agent=self.request.user)
        else:
            # Renvoyer tous les objets Bien si personne n'est connecté
            return DonneeCollectee.objects.all()
        

class DonneeCollecteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer

class SupportPublicitaireListView(generics.ListCreateAPIView):
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer

class SupportPublicitaireDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer

class MarqueListView(generics.ListCreateAPIView):
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer

class VisibiliteListView(generics.ListCreateAPIView):
    queryset = Visibilite.objects.all()
    serializer_class = VisibiliteSerializer

class EtatListView(generics.ListCreateAPIView):
    queryset = Etat.objects.all()
    serializer_class = EtatSerializer

class CanalListView(generics.ListCreateAPIView):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer

class SiteListView(generics.ListCreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer