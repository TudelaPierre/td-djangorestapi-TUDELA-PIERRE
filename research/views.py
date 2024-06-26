from rest_framework import viewsets
from .models import Chercheur, ProjetRecherche, Publication
from .serializers import ChercheurSerializer, ProjetRechercheSerializer, PublicationSerializer

class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

class ProjetRechercheViewSet(viewsets.ModelViewSet):
    queryset = ProjetRecherche.objects.all()
    serializer_class = ProjetRechercheSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
