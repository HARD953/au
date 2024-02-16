from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate, Cast
from django.db.models import FloatField
from .models import DonneeCollectee
from custumer.models import CustomUser

class StatsByAgent(APIView):
    def get(self, request, agent_id=None):
        # Sélectionner les statistiques pour tous les agents ou un agent spécifique
        agents_filter = {'agent_id': agent_id} if agent_id else {}
        agents = CustomUser.objects.filter(**agents_filter).values('id').distinct()

        # Initialiser un dictionnaire pour stocker les statistiques par agent
        stats_by_agent = {}

        # Définir les annotations communes pour éviter les répétitions
        annotate_stats = lambda queryset: queryset.annotate(
            total=Count('id'),
            total_tsp=Sum(Cast('TSP', output_field=FloatField())),
            total_odp=Sum(Cast('ODP_value', output_field=FloatField())),
            date=TruncDate('create')
        ).order_by('date')

        # Parcourir chaque agent et calculer les statistiques
        for agent_data in agents:
            agent_id = agent_data['id']
            agent_stats = {}

            # Statistiques par commune, entreprise, marque, état et date pour cet agent
            agent_stats['Commune'] = annotate_stats(
                DonneeCollectee.objects.filter(agent=agent_id).values('commune')
            )

            agent_stats['Commune_entreprise'] = annotate_stats(
                DonneeCollectee.objects.filter(agent=agent_id).values('commune', 'entreprise')
            )

            agent_stats['Commune_marque'] = annotate_stats(
                DonneeCollectee.objects.filter(agent=agent_id).values('commune', 'Marque')
            )

            agent_stats['Commune_etat'] = annotate_stats(
                DonneeCollectee.objects.filter(agent=agent_id).values('commune', 'etat_support')
            )

            # Autres statistiques peuvent être ajoutées ici
            # Stocker les statistiques dans le dictionnaire global
            stats_by_agent[agent_id] = agent_stats

        # Retourner les statistiques par agent
        return Response(stats_by_agent, status=status.HTTP_200_OK)
