from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import FloatField
from .models import*

class GTotalCollectedDataViewM(APIView):
    def get(self, request):
        if self.request.user.is_agent:
            # Agrégations générales
            nombre_total = DonneeCollectee.objects.count()
            montant_total_tsp = DonneeCollectee.objects.annotate(
                TSP_float=Cast('TSP', FloatField())
            ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
            montant_total_odp = DonneeCollectee.objects.annotate(
                ODP_value_float=Cast('ODP_value', FloatField())
            ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
            montant_total = montant_total_tsp + montant_total_odp

                # Fonction pour obtenir les montants pour une commune, une marque et un état donnés
            def get_montants_commune_marque_etat(commune, marque, etat):
                nombre_total_commune_marque_etat = DonneeCollectee.objects.filter(
                    commune=commune, Marque=marque, etat_support=etat
                ).count()
                montant_total_tsp_commune_marque_etat = DonneeCollectee.objects.filter(
                    commune=commune, Marque=marque, etat_support=etat
                ).aggregate(TSP_float=Sum(Cast('TSP', FloatField())))['TSP_float'] or 0
                montant_total_odp_commune_marque_etat = DonneeCollectee.objects.filter(
                    commune=commune, Marque=marque, etat_support=etat
                ).aggregate(ODP_value_float=Sum(Cast('ODP_value', FloatField())))['ODP_value_float'] or 0
                montant_total_commune_marque_etat = (
                    montant_total_tsp_commune_marque_etat + montant_total_odp_commune_marque_etat
                )
                return (
                    nombre_total_commune_marque_etat,
                    montant_total_tsp_commune_marque_etat,
                    montant_total_odp_commune_marque_etat,
                    montant_total_commune_marque_etat,
                )
                # Agrégations par commune, par marque et par état
            communes = DonneeCollectee.objects.values('commune').distinct()
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
                        (
                            nombre_total_commune_marque_etat,
                            montant_total_tsp_commune_marque_etat,
                            montant_total_odp_commune_marque_etat,
                            montant_total_commune_marque_etat
                        ) = get_montants_commune_marque_etat(commune, marque, etat)

                        marque_aggregations[etat] = {
                            'nombre_total': nombre_total_commune_marque_etat,
                            'montant_total_tsp': montant_total_tsp_commune_marque_etat,
                            'montant_total_odp': montant_total_odp_commune_marque_etat,
                            'montant_total': montant_total_commune_marque_etat,
                        }

                    commune_aggregations[marque] = marque_aggregations

                aggregations[commune] = commune_aggregations
            else:
                                # Agrégations générales
                nombre_total = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise).count()
                montant_total_tsp = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise).annotate(
                    TSP_float=Cast('TSP', FloatField())
                ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
                montant_total_odp = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise).annotate(
                    ODP_value_float=Cast('ODP_value', FloatField())
                ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
                montant_total = montant_total_tsp + montant_total_odp

                # Fonction pour obtenir les montants pour une commune, une marque et un état donnés
                def get_montants_commune_marque_etat(commune, marque, etat):
                    nombre_total_commune_marque_etat = DonneeCollectee.objects.filter(
                        entreprise=self.request.user.entreprise,
                        commune=commune, Marque=marque, etat_support=etat
                    ).count()
                    montant_total_tsp_commune_marque_etat = DonneeCollectee.objects.filter(
                        entreprise=self.request.user.entreprise,
                        commune=commune, Marque=marque, etat_support=etat
                    ).aggregate(TSP_float=Sum(Cast('TSP', FloatField())))['TSP_float'] or 0
                    montant_total_odp_commune_marque_etat = DonneeCollectee.objects.filter(
                        entreprise=self.request.user.entreprise,
                        commune=commune, Marque=marque, etat_support=etat
                    ).aggregate(ODP_value_float=Sum(Cast('ODP_value', FloatField())))['ODP_value_float'] or 0
                    montant_total_commune_marque_etat = (
                        montant_total_tsp_commune_marque_etat + montant_total_odp_commune_marque_etat
                    )
                    return (
                        nombre_total_commune_marque_etat,
                        montant_total_tsp_commune_marque_etat,
                        montant_total_odp_commune_marque_etat,
                        montant_total_commune_marque_etat,
                    )
                # Agrégations par commune, par marque et par état
                communes = DonneeCollectee.objects.values('commune').distinct()
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
                            (
                                nombre_total_commune_marque_etat,
                                montant_total_tsp_commune_marque_etat,
                                montant_total_odp_commune_marque_etat,
                                montant_total_commune_marque_etat
                            ) = get_montants_commune_marque_etat(commune, marque, etat)

                            marque_aggregations[etat] = {
                                'nombre_total': nombre_total_commune_marque_etat,
                                'montant_total_tsp': montant_total_tsp_commune_marque_etat,
                                'montant_total_odp': montant_total_odp_commune_marque_etat,
                                'montant_total': montant_total_commune_marque_etat,
                            }

                        commune_aggregations[marque] = marque_aggregations

                    aggregations[commune] = commune_aggregations

        return Response({
            # 'nombre_total': nombre_total,
            # 'montant_total_tsp': montant_total_tsp,
            # 'montant_total_odp': montant_total_odp,
            # 'montant_total': montant_total,

            'aggregations': aggregations,
        }, status=status.HTTP_200_OK)
