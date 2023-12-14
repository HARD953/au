# from .models import DonneeCollectee
# from django.db.models import*
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.db.models import Count, Avg, Sum
# from django.db.models.functions import TruncMonth
# from django.db.models import Max
# from .models import DonneeCollectee  # Assurez-vous d'importer votre modèle

# class TotalCollectedDataView(APIView):
#     def get(self, request):

#         average_ad_tax_per_month = DonneeCollectee.objects.annotate(month=TruncMonth('date_collecte')).values('month').annotate(average_tax=Avg('TSP'))
#         total_agents = DonneeCollectee.objects.values('agent').distinct().count()
#         collects_per_agent = DonneeCollectee.objects.values('agent').annotate(total=Count('agent'))
#         last_collection_date_per_agent = DonneeCollectee.objects.values('agent').annotate(last_collection=Max('date_collecte'))
#         total_ads_by_commune = DonneeCollectee.objects.values('commune').annotate(total=Count('commune'))
#         print(total_ads_by_commune)
#         total_lit_ads_by_commune = DonneeCollectee.objects.filter(visibilite='eclaire').values('commune').annotate(total=Count('commune'))
#         ads_by_support_type = DonneeCollectee.objects.values('type_support').annotate(total=Count('type_support'))
#         total_tax_by_support_type = DonneeCollectee.objects.values('type_support').annotate(total_tax=Sum('TSP'))
#         ads_by_condition = DonneeCollectee.objects.values('etat_support').annotate(total=Count('etat_support'))
#         percentage_ads_lit_by_commune = {}
#         for commune_data in total_ads_by_commune:
#             commune_name = commune_data['commune']
#             total_ads = commune_data['total']
           
#             percentage_ads_lit_by_commune[commune_name] = total_ads

#         return Response({'percentage_ads_lit_by_commune': percentage_ads_lit_by_commune,
#                          'total_collected_data': total_collected_data,
#                          'average_duration': average_duration,
#                          'total_ads_by_type': total_ads_by_type,
#                          'total_ad_tax': total_ad_tax,
#                          'total_odp': total_odp,
#                          'average_ad_tax_per_month': average_ad_tax_per_month,
#                          'total_agents': total_agents,
#                          'collects_per_agent': collects_per_agent,
#                          'last_collection_date_per_agent': last_collection_date_per_agent,
#                          'total_ads_by_state': total_ads_by_state,
#                          'total_ads_by_visibility': total_ads_by_visibility,
#                          'ads_by_support_type': ads_by_support_type,
#                          'total_tax_by_support_type': total_tax_by_support_type,
#                          'ads_by_condition': ads_by_condition
#                         }, status=status.HTTP_200_OK)



# # class AverageSurfaceView(APIView):
# #     def get(self, request):
# #         average_surface = DonneeCollectee.objects.aggregate(Avg('surface'))['surface__avg']
# #         return Response({'average_surface': average_surface}, status=status.HTTP_200_OK)

# # class AverageDurationView(APIView):
# #     def get(self, request):
# #         average_duration = DonneeCollectee.objects.aggregate(Avg('duree'))['duree__avg']
# #         return Response({'average_duration': average_duration}, status=status.HTTP_200_OK)
    
# # class TotalAdsByTypeView(APIView):
# #     def get(self, request):
# #         total_ads_by_type = DonneeCollectee.objects.values('type_site').annotate(total=Count('type_site'))
# #         return Response({'total_ads_by_type': total_ads_by_type}, status=status.HTTP_200_OK)
    
# # class TotalAdTaxView(APIView):
# #     def get(self, request):
# #         total_ad_tax = DonneeCollectee.objects.aggregate(Sum('TSP'))['TSP__sum']
# #         return Response({'total_ad_tax': total_ad_tax}, status=status.HTTP_200_OK)
    
# # class TotalODPView(APIView):
# #     def get(self, request):
# #         total_odp = DonneeCollectee.objects.aggregate(Sum('ODP'))['ODP__sum']
# #         return Response({'total_odp': total_odp}, status=status.HTTP_200_OK)

# # class AverageAdTaxPerMonthView(APIView):
# #     def get(self, request):
# #         average_ad_tax_per_month = DonneeCollectee.objects.annotate(month=TruncMonth('date_collecte')).values('month').annotate(average_tax=Avg('TSP'))
# #         return Response({'average_ad_tax_per_month': average_ad_tax_per_month}, status=status.HTTP_200_OK)
    
# # class TotalAgentsView(APIView):
# #     def get(self, request):
# #         total_agents = DonneeCollectee.objects.values('agent').distinct().count()
# #         return Response({'total_agents': total_agents}, status=status.HTTP_200_OK)

# # class CollectsPerAgentView(APIView):
# #     def get(self, request):
# #         collects_per_agent = DonneeCollectee.objects.values('agent').annotate(total=Count('agent'))
# #         return Response({'collects_per_agent': collects_per_agent}, status=status.HTTP_200_OK)
    
# # class LastCollectionDatePerAgentView(APIView):
# #     def get(self, request):
# #         last_collection_date_per_agent = DonneeCollectee.objects.values('agent').annotate(last_collection=Max('date_collecte'))
# #         return Response({'last_collection_date_per_agent': last_collection_date_per_agent}, status=status.HTTP_200_OK)
    
# # class TotalAdsByStateView(APIView):
# #     def get(self, request):
# #         total_ads_by_state = DonneeCollectee.objects.values('etat').annotate(total=Count('etat'))
# #         return Response({'total_ads_by_state': total_ads_by_state}, status=status.HTTP_200_OK)
    
# # class TotalSurfaceGoodConditionView(APIView):
# #     def get(self, request):
# #         total_surface_good_condition = DonneeCollectee.objects.filter(etat='en bon état').aggregate(Sum('surface'))['surface__sum']
# #         return Response({'total_surface_good_condition': total_surface_good_condition}, status=status.HTTP_200_OK)

# # class TotalAdsByVisibilityView(APIView):
# #     def get(self, request):
# #         total_ads_by_visibility = DonneeCollectee.objects.values('visibilite').annotate(total=Count('visibilite'))
# #         return Response({'total_ads_by_visibility': total_ads_by_visibility}, status=status.HTTP_200_OK)
    
# # class TotalAdsByOwnerView(APIView):
# #     def get(self, request):
# #         total_ads_by_owner = DonneeCollectee.objects.values('proprietaire').annotate(total=Count('proprietaire'))
# #         return Response({'total_ads_by_owner': total_ads_by_owner}, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Avg, Sum
from django.db.models.functions import TruncMonth
from django.db.models import Max, FloatField
from django.db.models.functions import Cast
from .models import DonneeCollectee

class TotalCollectedDataView(APIView):
    def get(self, request):
        # # Agrégations générales
        # nombre_total = DonneeCollectee.objects.count()
        # montant_total_tsp = DonneeCollectee.objects.annotate(
        #     TSP_float=Cast('TSP', FloatField())
        # ).aggregate(Sum('TSP_float'))['TSP_float__sum']
        # montant_total_odp = DonneeCollectee.objects.annotate(
        #     ODP_value_float=Cast('ODP_value', FloatField())
        # ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum']
        # montant_total = montant_total_tsp + montant_total_odp

        # # Agrégations par état_support
        # etats_support = ['Bon', 'Défraichis', 'Détérioré']
        # etats_aggregations = {}
        # for etat in etats_support:
        #     nombre_total_etat = DonneeCollectee.objects.filter(etat_support=etat).count()
        #     montant_total_etat_tsp = DonneeCollectee.objects.filter(etat_support=etat).annotate(
        #         TSP_float=Cast('TSP', FloatField())
        #     ).aggregate(Sum('TSP_float'))['TSP_float__sum']
        #     montant_total_etat_odp = DonneeCollectee.objects.filter(etat_support=etat).annotate(
        #         ODP_value_float=Cast('ODP_value', FloatField())
        #     ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum']
        #     montant_total_etat = montant_total_etat_tsp + montant_total_etat_odp

        #     etats_aggregations[etat] = {
        #         'nombre_total': nombre_total_etat,
        #         'montant_total_tsp': montant_total_etat_tsp,
        #         'montant_total_odp': montant_total_etat_odp,
        #         'montant_total': montant_total_etat,
        #     }

        # Agrégations par agent
        # agents_aggregations = {}
        # agents = DonneeCollectee.objects.values('agent').distinct()
        # for agent_data in agents:
        #     agent_id = agent_data['agent']
        #     agent_nombre_total = DonneeCollectee.objects.filter(agent=agent_id).count()
        #     agent_montant_total_tsp = DonneeCollectee.objects.filter(agent=agent_id).annotate(
        #         TSP_float=Cast('TSP', FloatField())
        #     ).aggregate(Sum('TSP_float'))['TSP_float__sum']
        #     agent_montant_total_odp = DonneeCollectee.objects.filter(agent=agent_id).annotate(
        #         ODP_value_float=Cast('ODP_value', FloatField())
        #     ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum']
        #     agent_montant_total = agent_montant_total_tsp + agent_montant_total_odp

        #     agents_aggregations[agent_id] = {
        #         'nombre_total': agent_nombre_total,
        #         'montant_total_tsp': agent_montant_total_tsp,
        #         'montant_total_odp': agent_montant_total_odp,
        #         'montant_total': agent_montant_total,
        #     }

        # Agrégations par commune
        if self.request.user.is_agent:
            communes_aggregations = {}
            communes = DonneeCollectee.objects.values('commune').distinct()
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for etat_support in ['Bon', 'Défraichis', 'Détérioré']:
                    nombre_total_etat = DonneeCollectee.objects.filter(commune=commune, etat_support=etat_support).count()
                    montant_total_etat_tsp = DonneeCollectee.objects.filter(commune=commune, etat_support=etat_support).annotate(
                        TSP_float=Cast('TSP', FloatField())
                    ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
                    montant_total_etat_odp = DonneeCollectee.objects.filter(commune=commune, etat_support=etat_support).annotate(
                        ODP_value_float=Cast('ODP_value', FloatField())
                    ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
                    montant_total_etat = montant_total_etat_tsp + montant_total_etat_odp

                    commune_aggregations[etat_support] = {
                        'nombre_total': nombre_total_etat,
                        'montant_total_tsp': montant_total_etat_tsp,
                        'montant_total_odp': montant_total_etat_odp,
                        'montant_total': montant_total_etat,
                    }

                communes_aggregations[commune] = commune_aggregations
        else:
            communes_aggregations = {}
            communes = DonneeCollectee.objects.filter(entreprise=self.request.user.entreprise).values('commune').distinct()
            for commune_data in communes:
                commune = commune_data['commune']
                commune_aggregations = {}
                for etat_support in ['Bon', 'Défraichis', 'Détérioré']:
                    nombre_total_etat = DonneeCollectee.objects.filter(commune=commune, etat_support=etat_support,entreprise=self.request.user.entreprise).count()
                    montant_total_etat_tsp = DonneeCollectee.objects.filter(commune=commune, etat_support=etat_support,entreprise=self.request.user.entreprise).annotate(
                        TSP_float=Cast('TSP', FloatField())
                    ).aggregate(Sum('TSP_float'))['TSP_float__sum'] or 0
                    montant_total_etat_odp = DonneeCollectee.objects.filter(commune=commune, etat_support=etat_support,entreprise=self.request.user.entreprise).annotate(
                        ODP_value_float=Cast('ODP_value', FloatField())
                    ).aggregate(Sum('ODP_value_float'))['ODP_value_float__sum'] or 0
                    montant_total_etat = montant_total_etat_tsp + montant_total_etat_odp

                    commune_aggregations[etat_support] = {
                        'nombre_total': nombre_total_etat,
                        'montant_total_tsp': montant_total_etat_tsp,
                        'montant_total_odp': montant_total_etat_odp,
                        'montant_total': montant_total_etat,
                    }

                communes_aggregations[commune] = commune_aggregations


        return Response({
            # 'nombre_total': nombre_total,
            # 'montant_total_tsp': montant_total_tsp,
            # 'montant_total_odp': montant_total_odp,
            # 'montant_total': montant_total,
            # 'etats_aggregations': etats_aggregations,
            # 'agents_aggregations': agents_aggregations,
            'communes_aggregations': communes_aggregations,
        }, status=status.HTTP_200_OK)
