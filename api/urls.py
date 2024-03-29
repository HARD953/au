from django.urls import path
from .views import *
from .stats import *
from .statis2 import *
from .marque1 import *
from .statagent import *
from .etatsupport import *

urlpatterns = [
    path('donneescollectees/', DonneeCollecteeList.as_view(), name='donnee-collectee-list'),
    path('donneescollecteesall/', DonneeCollecteeListAll.as_view(), name='donnee-collectee-list'),
    path('statbyetat/', StatByEtat.as_view(), name='stat-collectee-list'),
    path('statbyetatall/', StatByEtatAll.as_view(), name='stat-collectee-list'),
    path('all/', Allcollecte.as_view(), name='all-collectee-list'),
    path('donneescollectees/<int:pk>/', DonneeCollecteeDetailView.as_view(), name='donnee-collectee-detail'),
    path('collectedata/', DonneeCollecteeCreate.as_view(), name='donnee-collectee-create'),
    path('commune/', CommuneL.as_view(), name='commune-collectee-create'),
    path('commune/<int:pk>/', CommuneDetail.as_view(), name='commune-collectee-detail'),
    path('communeapp/', CommuneApp.as_view(), name='commune-collectee-app'),
    path('etat/', EtatListView.as_view(), name='etat'),
    path('visibilite/', VisibiliteListView.as_view(), name='visibilite'),
    path('canal/', CanalListView.as_view(), name='canal'),
    path('marque/', MarqueListView.as_view(), name='marque'),
    path('site/', SiteListView.as_view(), name='site'),
    path('etat/<int:pk>/', EtatListViewD.as_view(), name='etat'),
    path('visibilite/<int:pk>/', VisibiliteListViewD.as_view(), name='visibilite'),
    path('canal/<int:pk>/', CanalListViewD.as_view(), name='canal'),
    path('marque/<int:pk>/', MarqueListViewD.as_view(), name='marque'),
    path('site/<int:pk>/', SiteListViewD.as_view(), name='site'),

    path('supports/', SupportPublicitaireListView.as_view(), name='support-publicitaire-list'),
    path('supports/<int:pk>/', SupportPublicitaireDetailView.as_view(), name='support-publicitaire-detail'),
    
    # # Statistiques générales
    path('statagent/<str:start_date>/<str:end_date>/', StatsByAgent.as_view(), name='general-agent'),
    path('statagentid/<str:start_date>/<str:end_date>/<int:agent_id>/', StatsByAgent.as_view(), name='general-agents'),
    path('gcollecte/<str:start_date>/<str:end_date>/', GTotalCollectedDataView.as_view(), name='general-statistics'),
    path('collecte/<str:start_date>/<str:end_date>/', TotalCollectedDataView.as_view(), name='statistics-etat'),
    path('collectem/<str:start_date>/<str:end_date>/', GTotalCollectedDataViewM.as_view(), name='statistics-marque'),
]
