from rest_framework import serializers
from .models import SpecificItem, VagueItem

class SpecificItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificItem
        fields = '__all__'

class VagueItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VagueItem
        fields = '__all__'
