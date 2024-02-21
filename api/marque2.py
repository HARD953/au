from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Avg, Sum
from django.db.models.functions import TruncMonth
from django.db.models import Max, FloatField
from django.db.models.functions import Cast
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate
from django.db.models import FloatField, F
from .models import *
from datetime import datetime

class GTotalCollectedDataViewM(APIView):
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

        if self.request.user.is_agent:
            # Agrégations générales
            nombre_total = DonneeCollectee.objects.filter(**date_filters).count()
            montant_total_tsp = DonneeCollectee.objects.filter(**date_filters).annotate(
                TSP_float=Cast('TSP', FloatField())
            ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
            montant_total_odp = DonneeCollectee.objects.filter(**date_filters).annotate(
                ODP_value_float=Cast('ODP_value', FloatField())
            ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
            montant_total = montant_total_tsp + montant_total_odp

            # Fonction pour obtenir les montants pour une commune, une marque et un état donnés
            def get_montants_commune_marque_etat(commune, marque, etat):
                montants_commune_marque_etat = DonneeCollectee.objects.filter(
                    commune=commune, Marque=marque, etat_support=etat, **date_filters
                ).annotate(
                    date=TruncDate('create')
                ).values('date').annotate(
                    nombre_total=Count('id'),
                    montant_total_tsp=Sum(Cast('TSP', FloatField())),
                    montant_total_odp=Sum(Cast('ODP_value', FloatField())),
                    montant_total=Sum(Cast('TSP', FloatField())) + Sum(Cast('ODP_value', FloatField()))
                )
                return montants_commune_marque_etat

            # Agrégations par commune, par marque et par état
            communes = DonneeCollectee.objects.filter(**date_filters).values('commune').distinct()
            marques = Marque.objects.values('marque').distinct()
            etats_support = ['Bon', 'Défraichis', 'Détérioré']
            aggregations = {}
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for marque_data in marques:
                    marque = marque_data['marque']
                    marque_aggregations = {}
                    for etat in etats_support:
                        montants_commune_marque_etat = get_montants_commune_marque_etat(commune, marque, etat)
                        marque_aggregations[etat] = montants_commune_marque_etat

                    commune_aggregations[marque] = marque_aggregations

                aggregations[commune] = commune_aggregations
        else:
            # Agrégations générales
            nombre_total = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise, **date_filters).count()
            montant_total_tsp = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise, **date_filters).annotate(
                TSP_float=Cast('TSP', FloatField())
            ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
            montant_total_odp = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise, **date_filters).annotate(
                ODP_value_float=Cast('ODP_value', FloatField())
            ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
            montant_total = montant_total_tsp + montant_total_odp

            # Fonction pour obtenir les montants pour une commune, une marque et un état donnés
            def get_montants_commune_marque_etat(commune, marque, etat):
                montants_commune_marque_etat = DonneeCollectee.objects.filter(
                    entreprise=self.request.user.entreprise, commune=commune, Marque=marque, etat_support=etat, **date_filters
                ).annotate(
                    date=TruncDate('create')
                ).values('date').annotate(
                    nombre_total=Count('id'),
                    montant_total_tsp=Sum(Cast('TSP', FloatField())),
                    montant_total_odp=Sum(Cast('ODP_value', FloatField())),
                    montant_total=Sum(Cast('TSP', FloatField())) + Sum(Cast('ODP_value', FloatField()))
                )
                return montants_commune_marque_etat

            # Agrégations par commune, par marque et par état
            communes = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise, **date_filters).values('commune').distinct()
            marques = Marque.objects.values('marque').distinct()
            etats_support = ['Bon', 'Défraichis', 'Détérioré']
            aggregations = {}
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for marque_data in marques:
                    marque = marque_data['marque']
                    marque_aggregations = {}
                    for etat in etats_support:
                        montants_commune_marque_etat = get_montants_commune_marque_etat(commune, marque, etat)
                        marque_aggregations[etat] = montants_commune_marque_etat

                    commune_aggregations[marque] = marque_aggregations

                aggregations[commune] = commune_aggregations

        return Response({
            'aggregations': aggregations,
        }, status=status.HTTP_200_OK)
