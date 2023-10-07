# api/urls.py

from django.urls import path
from .views import*


urlpatterns = [
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),  # Liste et création d'utilisateurs
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Détails, mise à jour et suppression d'un utilisateur
    # ... Autres URL pour d'autres vues si nécessaire
]
