from rest_framework import serializers
from database.models import ArtWork, Artist, Purchaser 


class ArtWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWork
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class PurchaserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchaser
        fields = '__all__'