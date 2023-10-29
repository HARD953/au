# api/models.py

from django.db import models
from custumer.models import CustomUser

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
    agent= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    entreprise= models.CharField(max_length=50)
    Marque= models.CharField(max_length=50)
    commune= models.CharField(max_length=50)
    type_support= models.CharField(max_length=50)
    surface= models.CharField(max_length=50)
    canal= models.CharField(max_length=50)
    etat_support= models.CharField(max_length=50)
    visibilite= models.CharField(max_length=50)
    description= models.CharField(max_length=50)
    observation= models.CharField(max_length=50)
    date_collecte = models.DateTimeField(auto_now_add=True)
    # proprietaire = models.CharField(max_length=50)
    # image_support = models.ImageField(upload_to='collecte_images/', null=True, blank=True)
    duree=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    longueur= models.DecimalField(max_digits=9, decimal_places=6)
    largeur= models.DecimalField(max_digits=9, decimal_places=6)
    TSP = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    ODP = models.BooleanField(default=False)  # Champ ODP
    ODP_value = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calculer le TSP en multipliant la surface par la durée
        self.TSP = self.largeur * self.longueur * self.duree
        if self.ODP:
            self.ODP_value =  self.largeur*self.longueur * self.duree
        else:
            self.ODP_value = 0
        super(DonneeCollectee, self).save(*args, **kwargs)
    
    # Ajoutez d'autres champs pour les données collectées, comme des statistiques, etc.

    def __str__(self):
        return f"Donnée #{self.id} pour {self.type_support}"
