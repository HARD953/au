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

class DonneeCollecteeCreate(generics.CreateAPIView):
    queryset = DonneeCollectee.objects.all()
    serializer_class = DonneeCollecteeSerializer1
    def perform_create(self, serializer):
        # Appeler la méthode perform_create du parent pour effectuer la création
        instance = serializer.save()
        # Ajouter un message personnalisé
        message = f"Donnée #{instance.id} pour {instance.type_support} a été créée avec succès."
        # Vous pouvez également ajouter d'autres messages ou des détails supplémentaires
        # Envoyer une réponse avec le message
        return Response({'message': message}, status=status.HTTP_201_CREATED)
    
    # permission_classes = [IsAuthenticated]
    # def perform_create(self, serializer):
    #     # Associer l'utilisateur connecté comme propriétaire du Bien
    #     if self.request.user.is_anonymous:
    #         serializer.save()
    #     else:
    #         serializer.save(agent=self.request.user)

class DonneeCollecteeList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DonneeCollecteeSerializer# Assurez-vous que l'utilisateur est authentifié
    def get_queryset(self):
        # Filtrer les objets DonneeCollectee pour l'utilisateur connecté et l'entreprise associée
        user = self.request.user
        if user.is_agent:  # Vérifie si l'utilisateur est connecté
            return DonneeCollectee.objects.all()
        else:
            return DonneeCollectee.objects.filter(entreprise=user.entreprise)
               
class DonneeCollecteeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonneeCollecteeSerializer
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # Filtrer les objets Bien pour l'utilisateur connecté
            return DonneeCollectee.objects.filter(agent=self.request.user)
        else:
            # Renvoyer tous les objets Bien si personne n'est connecté
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


