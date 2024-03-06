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

class DonneeCollecteeCreate(generics.CreateAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer1
    
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
        if user.is_agent:  # Vérifie si l'utilisateur est connecté
            return DonneeCollectee.objects.all()
        elif user.is_recenseur:
            current_date = datetime.now().date()
            return DonneeCollectee.objects.filter(agent=user,create__date=current_date)
        else:
            return DonneeCollectee.objects.filter(entreprise=user.entreprise)
        
class DonneeCollecteeListAll(generics.ListAPIView):
    permission_classes = [IsAuthenticated] 
    serializer_class = DonneeCollecteeSerializer# Assurez-vous que l'utilisateur est authentifié
    def get_queryset(self):
        # Filtrer les objets DonneeCollectee pour l'utilisateur connecté et l'entreprise associée
        user = self.request.user
        return DonneeCollectee.objects.filter(agent=user)

class Allcollecte(generics.ListAPIView):
    permission_classes = [IsAuthenticated] 
    serializer_class = DonneeCollecteeSerializer# Assurez-vous que l'utilisateur est authentifié
    def get_queryset(self):
        # Filtrer les objets DonneeCollectee pour l'utilisateur connecté et l'entreprise associée
        user = self.request.user
        return DonneeCollectee.objects.filter(agent=user)

           
class DonneeCollecteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonneeCollecteeSerializer
    def get_queryset(self):
        return DonneeCollectee.objects.all()
        
class NombreSupportsParAgent(APIView):
    def get(self, request):
        # Vérifiez si l'utilisateur est authentifié
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Obtenez le nombre de supports collectés par agent
        supports_par_agent = DonneeCollectee.objects.filter(agent=request.user).values('agent').annotate(nombre_supports=Count('id'))

        # supports_par_agent est maintenant une liste de dictionnaires avec 'agent' et 'nombre_supports'
        for entry in supports_par_agent:
            agent = entry['agent']
            nombre_supports = entry['nombre_supports']
            return Response({'agent': agent, 'nombre_supports': nombre_supports}, status=status.HTTP_200_OK)
        

class DonneeCollecteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer

class SupportPublicitaireListView(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia] 
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer

class SupportPublicitaireDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsLanfia] 
    queryset = SupportPublicitaire.objects.all()
    serializer_class = SupportPublicitaireSerializer

class MarqueListView(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer

class MarqueListViewD(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsLanfia]
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer

class VisibiliteListView(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Visibilite.objects.all()
    serializer_class = VisibiliteSerializer

class VisibiliteListViewD(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsLanfia]
    queryset = Visibilite.objects.all()
    serializer_class = VisibiliteSerializer

class EtatListView(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Etat.objects.all()
    serializer_class = EtatSerializer

class EtatListViewD(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsLanfia]
    queryset = Etat.objects.all()
    serializer_class = EtatSerializer

class CanalListView(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer

class CanalListViewD(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsLanfia]
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer

class SiteListView(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteListViewD(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsLanfia]
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class CommuneL(generics.ListCreateAPIView):
    # permission_classes = [IsLanfia]
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializers

class CommuneDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsLanfia]
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializers

class CommuneApp(generics.ListAPIView):
    # permission_classes = [IsLanfia]
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializersApp


