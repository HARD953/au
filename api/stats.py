from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Avg, Sum
from django.db.models.functions import TruncMonth
from django.db.models import Max, FloatField
from django.db.models.functions import Cast
from .models import DonneeCollectee
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from django.db.models import FloatField, F
from .models import DonneeCollectee

class TotalCollectedDataView(APIView):
    def get(self, request):
        # Agrégations par commune
        if self.request.user.is_agent:
            communes_aggregations = {}
            communes = DonneeCollectee.objects.values('commune').distinct()
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for etat_support in ['Bon', 'Défraichis', 'Détérioré']:
                    commune_etat_aggregations = DonneeCollectee.objects.filter(
                        commune=commune, etat_support=etat_support
                    ).annotate(
                        date=TruncDate('create')
                    ).values('date').annotate(
                        nombre_total=Count('id'),
                        montant_total_tsp=Sum(Cast('TSP', FloatField())),
                        montant_total_odp=Sum(Cast('ODP_value', FloatField())),
                        montant_total=Sum(Cast('TSP', FloatField())) + Sum(Cast('ODP_value', FloatField()))
                    )
                    commune_aggregations[etat_support] = commune_etat_aggregations

                communes_aggregations[commune] = commune_aggregations
        else:
            communes_aggregations = {}
            communes = DonneeCollectee.objects.filter(
                entreprise=self.request.user.entreprise
            ).values('commune').distinct()
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for etat_support in ['Bon', 'Défraichis', 'Détérioré']:
                    commune_etat_aggregations = DonneeCollectee.objects.filter(
                        commune=commune, etat_support=etat_support, entreprise=self.request.user.entreprise
                    ).annotate(
                        date=TruncDate('create')
                    ).values('date').annotate(
                        nombre_total=Count('id'),
                        montant_total_tsp=Sum(Cast('TSP', FloatField())),
                        montant_total_odp=Sum(Cast('ODP_value', FloatField())),
                        montant_total=Sum(Cast('TSP', FloatField())) + Sum(Cast('ODP_value', FloatField()))
                    )
                    commune_aggregations[etat_support] = commune_etat_aggregations

                communes_aggregations[commune] = commune_aggregations

        return Response({
            'communes_aggregations': communes_aggregations,
        }, status=status.HTTP_200_OK)
