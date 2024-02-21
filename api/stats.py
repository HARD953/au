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
from datetime import datetime

class TotalCollectedDataView(APIView):
    def get(self, request, start_date=None, end_date=None):
        # Convertir les dates en objets date si elles sont fournies
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        # Définir les filtres de date en fonction des paramètres fournis
        date_filters = {}
        if start_date:
            date_filters['create__date__gte'] = start_date
        if end_date:
            date_filters['create__date__lte'] = end_date

        # Agrégations par commune avec les filtres de date
        if self.request.user.is_agent:
            communes_aggregations = {}
            communes = DonneeCollectee.objects.filter(**date_filters).values('commune').distinct()
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for etat_support in ['Bon', 'Défraichis', 'Détérioré']:
                    commune_etat_aggregations = DonneeCollectee.objects.filter(
                        commune=commune, etat_support=etat_support, **date_filters
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
                entreprise=self.request.user.entreprise, **date_filters
            ).values('commune').distinct()
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for etat_support in ['Bon', 'Défraichis', 'Détérioré']:
                    commune_etat_aggregations = DonneeCollectee.objects.filter(
                        commune=commune, etat_support=etat_support, entreprise=self.request.user.entreprise,
                        **date_filters
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
