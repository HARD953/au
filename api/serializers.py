from rest_framework import serializers
from .models import *

class DonneeCollecteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonneeCollectee
        fields = '__all__'


class SupportPublicitaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportPublicitaire
        fields = '__all__'
