# api/models.py
from django.dispatch import receiver
from django.db import models
from custumer.models import CustomUser
from django.db.models.signals import pre_save
from django.utils import timezone

class SupportPublicitaire(models.Model):
    type_support = models.CharField(max_length=50)
    longueur= models.CharField(max_length=50)
    largeur= models.CharField(max_length=50)
    taux=models.IntegerField()
    def __str__(self):
        return self.type_support
    
class Marque(models.Model):
    marque = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.marque
    
class Canal(models.Model):
    canal = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.canal
    
class Site(models.Model):
    site = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.site
    
class Etat(models.Model):
    etat = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.etat
    
class Visibilite(models.Model):
    visibilite = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.visibilite

class Commune(models.Model):
    commune = models.CharField(max_length=50,default="Abidjan")
    tauxODP = models.CharField(max_length=50,default="6")
    tauxTSP = models.CharField(max_length=50,default="7")
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commune

class DonneeCollectee(models.Model):
    agent=models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=1)
    entreprise = models.CharField(max_length=50, blank=True)
    Marque = models.CharField(max_length=50, blank=True)
    commune = models.CharField(max_length=50, blank=True)  # Utilise ForeignKey pour lier à la table Commune
    type_support = models.CharField(max_length=50, blank=True)
    surface = models.CharField(max_length=50, blank=True)
    surfaceODP = models.CharField(max_length=50, blank=True)
    canal = models.CharField(max_length=50, blank=True)
    etat_support = models.CharField(max_length=50, blank=True)
    typesite = models.CharField(max_length=50, blank=True)
    visibilite = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    observation = models.CharField(max_length=50, blank=True)
    date_collecte = models.DateTimeField(auto_now_add=True, blank=True)
    image_support = models.ImageField(upload_to='collecte_images/', null=True, blank=True)
    duree = models.CharField(max_length=50, blank=True)
    TSP = models.CharField(max_length=50, default=12, blank=True)
    ODP = models.BooleanField(default=False, blank=True)
    ODP_value = models.CharField(max_length=50, default=1, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)

    def save(self, *args, **kwargs):
        # Récupérer les taux en fonction de la commune
        taux_commune = Commune.objects.get(commune=self.commune)
        self.tauxODP = taux_commune.tauxODP
        self.tauxTSP = taux_commune.tauxTSP
        # Calculer le TSP en multipliant la surface par la durée
        self.TSP = float(self.surface) * float(self.duree) * float(self.tauxTSP)
        if self.ODP:
            self.ODP_value = float(self.surfaceODP) * float(self.duree) * float(self.tauxODP)
        else:
            self.ODP_value = 0

        super(DonneeCollectee, self).save(*args, **kwargs)

    def __str__(self):
        return f"Donnée #{self.id} pour {self.type_support}"


# def calculate_tsp(instance):
#     return instance.surface * instance.duree * 7

# def calculate_odp_value(instance):
#     return instance.surfaceODP * instance.duree * 7 if instance.ODP else 0

# @receiver(pre_save, sender=DonneeCollectee)
# def update_tsp_and_odp_value(sender, instance, **kwargs):
#     instance.TSP = calculate_tsp(instance)
#     instance.ODP_value = calculate_odp_value(instance)
    
    # Ajoutez d'autres champs pour les données collectées, comme des statistiques, etc.

    
