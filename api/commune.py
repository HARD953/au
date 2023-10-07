from django.db.models import*
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DonneeCollectee

class AverageSurfaceByRegionView(APIView):
    def get(self, request):
        average_surface_by_region = DonneeCollectee.objects.values('region').annotate(average_surface=Avg('surface'))
        return Response({'average_surface_by_region': average_surface_by_region}, status=status.HTTP_200_OK)


class PercentageAdsLitByRegionView(APIView):
    def get(self, request):
        total_ads_by_region = DonneeCollectee.objects.values('region').annotate(total=Count('region'))
        total_lit_ads_by_region = DonneeCollectee.objects.filter(visibilite='éclairé').values('region').annotate(total=Count('region'))
        
        percentage_ads_lit_by_region = {}
        for region_data in total_ads_by_region:
            region_name = region_data['region']
            total_ads = region_data['total']
            total_lit_ads = next((item['total'] for item in total_lit_ads_by_region if item['region'] == region_name), 0)
            percentage = (total_lit_ads / total_ads) * 100 if total_ads > 0 else 0
            percentage_ads_lit_by_region[region_name] = round(percentage, 2)
        
        return Response({'percentage_ads_lit_by_region': percentage_ads_lit_by_region}, status=status.HTTP_200_OK)
