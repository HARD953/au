from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from custumer.models import*
from custumer.serializers import UserSerializer1

class DonneeCollecteeCreate(generics.CreateAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        # Associer l'utilisateur connecté comme propriétaire du Bien
        if self.request.user.is_anonymous:
            serializer.save()
        else:
            serializer.save(agent=self.request.user)

class DonneeCollecteeList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DonneeCollecteeSerializer# Assurez-vous que l'utilisateur est authentifié
    def get_queryset(self):
        # Filtrer les objets DonneeCollectee pour l'utilisateur connecté et l'entreprise associée
        user = self.request.user
        if user.is_user:  # Vérifie si l'utilisateur est connecté
            return DonneeCollectee.objects.filter(entreprise=user.entreprise)
        else:
            return DonneeCollectee.objects.none()
               
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

class CommuneL(generics.ListCreateAPIView):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializers

class CommuneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializers

class CommuneApp(generics.ListAPIView):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializersApp

class EntrepriseLists(generics.ListAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = EntrepriseSerializers

