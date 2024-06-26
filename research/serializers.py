from rest_framework import serializers
from .models import Chercheur, ProjetRecherche, Publication

class ChercheurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chercheur
        fields = '__all__'

class ProjetRechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetRecherche
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
