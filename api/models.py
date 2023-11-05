# api/models.py
from django.dispatch import receiver
from django.db import models
from custumer.models import CustomUser
from django.db.models.signals import pre_save

class SupportPublicitaire(models.Model):
    type_support = models.CharField(max_length=50)
    longueur= models.CharField(max_length=50)
    largeur= models.CharField(max_length=50)
    taux=models.IntegerField()
    def __str__(self):
        return self.type_support
    
class Marque(models.Model):
    marque = models.CharField(max_length=50)
    def __str__(self):
        return self.marque
    
class Canal(models.Model):
    canal = models.CharField(max_length=50)
    def __str__(self):
        return self.canal
    
class Site(models.Model):
    site = models.CharField(max_length=50)
    def __str__(self):
        return self.site
    
class Etat(models.Model):
    etat = models.CharField(max_length=50)
    def __str__(self):
        return self.etat
    
class Visibilite(models.Model):
    visibilite = models.CharField(max_length=50)
    def __str__(self):
        return self.visibilite

class DonneeCollectee(models.Model):
    agent = models.ForeignKey(CustomUser, on_delete=models.CASCADE,blank=True,default="issa@gmail.com")
    entreprise = models.CharField(max_length=50)
    Marque = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    type_support = models.CharField(max_length=50)
    surface = models.FloatField()
    surfaceODP = models.FloatField()
    canal = models.CharField(max_length=50)
    etat_support = models.CharField(max_length=50)
    visibilite = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    observation = models.CharField(max_length=50)
    date_collecte = models.DateTimeField(auto_now_add=True)
    image_support = models.ImageField(upload_to='collecte_images/', null=True, blank=True)
    duree = models.FloatField()
    TSP = models.FloatField(blank=True)
    ODP = models.BooleanField(default=False)
    ODP_value = models.FloatField(blank=True)

    def save(self, *args, **kwargs):
        # Calculer le TSP en multipliant la surface par la durée
        self.TSP = self.surface*self.duree
        if self.ODP:
            self.ODP_value =  self.surfaceODP*self.duree
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

    
