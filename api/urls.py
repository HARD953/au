from django.urls import path
from .views import *
from .stats import *

urlpatterns = [
    path('donneescollectees/', DonneeCollecteeListView.as_view(), name='donnee-collectee-list-create'),
    path('collectedata/', DonneeCollecteeCreateView.as_view(), name='donnee-collectee-list-create'),
    path('donneescollectees/<int:pk>/', DonneeCollecteeDetailView.as_view(), name='donnee-collectee-detail'),
    path('supports/', SupportPublicitaireListView.as_view(), name='support-publicitaire-list'),
    path('supports/<int:pk>/', SupportPublicitaireDetailView.as_view(), name='support-publicitaire-detail'),
    path('etat/', EtatListView.as_view(), name='etat'),
    path('visibilite/', VisibiliteListView.as_view(), name='visibilite'),
    path('canal/', CanalListView.as_view(), name='canal'),
    path('marque/', MarqueListView.as_view(), name='marque'),
    path('site/', SiteListView.as_view(), name='site'),

    # Statistiques générales
    path('collecte/', TotalCollectedDataView.as_view(), name='general-statistics'),
    # # Statistiques par emplacement géographique
    # path('api/statistiques/geographique/', AverageSurfaceView.as_view(), name='geographical-statistics'),
    # # Statistiques par type de support publicitaire
    # path('api/statistiques/support-publicitaire/', AverageDurationView.as_view(), name='support-statistics'),
    # # Statistiques sur la taxation
    # path('api/statistiques/taxation/', TotalAdsByTypeView.as_view(), name='taxation-statistics'),
    # # Statistiques par emplacement géographique
    # path('api/statistiques/geographique/', TotalAdTaxView.as_view(), name='geographical-statistics'),
    # # Statistiques par type de support publicitaire
    # path('api/statistiques/support-publicitaire/', TotalODPView.as_view(), name='support-statistics'),
    # # Statistiques sur la taxation
    # path('api/statistiques/taxation/', AverageAdTaxPerMonthView.as_view(), name='taxation-statistics'),
    # # Statistiques sur l'utilisation de l'application
    # path('api/statistiques/utilisation/', TotalAgentsView.as_view(), name='application-usage-statistics'),
    # # Statistiques sur l'état des supports publicitaires
    # path('api/statistiques/etat-support/', CollectsPerAgentView.as_view(), name='support-condition-statistics'),
    # # Statistiques sur la visibilité
    # path('api/statistiques/visibilite/', LastCollectionDatePerAgentView.as_view(), name='visibility-statistics'),
    # # Statistiques par propriétaire
    # path('api/statistiques/proprietaire/', TotalAdsByStateView.as_view(), name='owner-statistics'),
]
