from django.urls import path
from .views import *

urlpatterns = [
    path('donneescollectees/', DonneeCollecteeListCreateView.as_view(), name='donnee-collectee-list-create'),
    path('donneescollectees/<int:pk>/', DonneeCollecteeDetailView.as_view(), name='donnee-collectee-detail'),
    path('supports/', SupportPublicitaireListView.as_view(), name='support-publicitaire-list'),
    path('supports/<int:pk>/', SupportPublicitaireDetailView.as_view(), name='support-publicitaire-detail'),
]
