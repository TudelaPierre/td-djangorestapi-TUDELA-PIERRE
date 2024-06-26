from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChercheurViewSet, ProjetRechercheViewSet, PublicationViewSet

router = DefaultRouter()
router.register(r'chercheur', ChercheurViewSet)
router.register(r'projetRecherche', ProjetRechercheViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
