from django.urls import path
from .views import *

urlpatterns = [
    path('donneescollectees/', DonneeCollecteeListCreateView.as_view(), name='donnee-collectee-list-create'),
    path('donneescollectees/<int:pk>/', DonneeCollecteeDetailView.as_view(), name='donnee-collectee-detail'),
    path('supports/', SupportPublicitaireListView.as_view(), name='support-publicitaire-list'),
    path('supports/<int:pk>/', SupportPublicitaireDetailView.as_view(), name='support-publicitaire-detail'),
    path('etat/', EtatListView.as_view(), name='etat'),
    path('visibilite/', VisibiliteListView.as_view(), name='visibilite'),
    path('canal/', CanalListView.as_view(), name='canal'),
    path('marque/', MarqueListView.as_view(), name='marque'),
    path('site/', SiteListView.as_view(), name='site'),
]
