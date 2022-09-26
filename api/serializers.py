from rest_framework import serializers
from database.models import ArtWork


class ArtWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtWork
        fields = '__all__'