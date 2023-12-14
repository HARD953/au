from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import FloatField
from .models import DonneeCollectee

class GTotalCollectedDataView(APIView):
    def get(self, request):
        # Agrégations générales
        if self.request.user.is_agent:
            print(self.request.user.entreprise)
            nombre_total = DonneeCollectee.objects.count()
            montant_total_tsp = DonneeCollectee.objects.annotate(
                TSP_float=Cast('TSP', FloatField())
            ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
            montant_total_odp = DonneeCollectee.objects.annotate(
                ODP_value_float=Cast('ODP_value', FloatField())
            ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
            montant_total = montant_total_tsp + montant_total_odp

            # Fonction pour obtenir les montants pour un état_support donné
            def get_montants(etat_support):
                nombre_total_etat = DonneeCollectee.objects.filter(etat_support=etat_support).count()
                montant_total_tsp_etat = DonneeCollectee.objects.filter(etat_support=etat_support).aggregate(
                    TSP_float=Sum(Cast('TSP', FloatField()))
                )['TSP_float'] or 0
                montant_total_odp_etat = DonneeCollectee.objects.filter(etat_support=etat_support).aggregate(
                    ODP_value_float=Sum(Cast('ODP_value', FloatField()))
                )['ODP_value_float'] or 0
                montant_total_etat = montant_total_tsp_etat + montant_total_odp_etat
                return nombre_total_etat, montant_total_tsp_etat, montant_total_odp_etat, montant_total_etat

            # Agrégations par état_support
            (
                nombre_total_bon,
                montant_total_bon_tsp,
                montant_total_bon_odp,
                montant_total_bon
            ) = get_montants('Bon')

            (
                nombre_total_Defraichis,
                montant_total_Defraichis_tsp,
                montant_total_Defraichis_odp,
                montant_total_Defraichis
            ) = get_montants('Défraichis')

            (
                nombre_total_Deteriore,
                montant_total_Deteriore_tsp,
                montant_total_Deteriore_odp,
                montant_total_Deteriore
            ) = get_montants('Détérioré')
        else:
            print(self.request.user.entreprise)
            nombre_total = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise).count()
            montant_total_tsp = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise).annotate(
                TSP_float=Cast('TSP', FloatField())
            ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
            montant_total_odp = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise).annotate(
                ODP_value_float=Cast('ODP_value', FloatField())
            ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
            montant_total = montant_total_tsp + montant_total_odp

            # Fonction pour obtenir les montants pour un état_support donné
            def get_montants(etat_support):
                nombre_total_etat = DonneeCollectee.objects.filter(etat_support=etat_support,entreprise=self.request.user.entreprise).count()
                montant_total_tsp_etat = DonneeCollectee.objects.filter(etat_support=etat_support,entreprise=self.request.user.entreprise).aggregate(
                    TSP_float=Sum(Cast('TSP', FloatField()))
                )['TSP_float'] or 0
                montant_total_odp_etat = DonneeCollectee.objects.filter(etat_support=etat_support,entreprise=self.request.user.entreprise).aggregate(
                    ODP_value_float=Sum(Cast('ODP_value', FloatField()))
                )['ODP_value_float'] or 0
                montant_total_etat = montant_total_tsp_etat + montant_total_odp_etat
                return nombre_total_etat, montant_total_tsp_etat, montant_total_odp_etat, montant_total_etat

            # Agrégations par état_support
            (
                nombre_total_bon,
                montant_total_bon_tsp,
                montant_total_bon_odp,
                montant_total_bon
            ) = get_montants('Bon')

            (
                nombre_total_Defraichis,
                montant_total_Defraichis_tsp,
                montant_total_Defraichis_odp,
                montant_total_Defraichis
            ) = get_montants('Défraichis')

            (
                nombre_total_Deteriore,
                montant_total_Deteriore_tsp,
                montant_total_Deteriore_odp,
                montant_total_Deteriore
            ) = get_montants('Détérioré')
            

        return Response({
            'nombre_total': nombre_total,
            'montant_total_tsp': montant_total_tsp,
            'montant_total_odp': montant_total_odp,
            'montant_total': montant_total,

            'nombre_total_bon': nombre_total_bon,
            'montant_total_bon_tsp': montant_total_bon_tsp,
            'montant_total_bon_odp': montant_total_bon_odp,
            'montant_total_bon': montant_total_bon,

            'nombre_total_Defraichis': nombre_total_Defraichis,
            'montant_total_Defraichis_tsp': montant_total_Defraichis_tsp,
            'montant_total_Defraichis_odp': montant_total_Defraichis_odp,
            'montant_total_Defraichis': montant_total_Defraichis,

            'nombre_total_Deteriore': nombre_total_Deteriore,
            'montant_total_Deteriore_tsp': montant_total_Deteriore_tsp,
            'montant_total_Deteriore_odp': montant_total_Deteriore_odp,
            'montant_total_Deteriore': montant_total_Deteriore
        }, status=status.HTTP_200_OK)
