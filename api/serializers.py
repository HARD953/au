from rest_framework import serializers
from .models import *

class DonneeCollecteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeCollectee
        exclude = ['tauxODP', 'tauxTSP']
        
class TauxODPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeCollectee
        fields = ["tauxODP"]

class TauxTSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeCollectee
        fields = ["tauxTSP"]

class SupportPublicitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportPublicitaire
        fields = '__all__'

class VisibiliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visibilite
        fields = '__all__'
class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marque
        fields = '__all__'
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = '__all__'

class EtatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etat
        fields = '__all__'
