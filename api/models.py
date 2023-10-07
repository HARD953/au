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

class DonneeCollectee(models.Model):
    agent= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    marque= models.CharField(max_length=50)
    support_publicitaire = models.ForeignKey(SupportPublicitaire, on_delete=models.CASCADE)
    commune= models.CharField(max_length=50)
    canal= models.CharField(max_length=50)
    type_site= models.CharField(max_length=50)
    etat= models.CharField(max_length=50)
    visibilite= models.CharField(max_length=50)
    description= models.CharField(max_length=50)
    date_collecte = models.DateTimeField(auto_now_add=True)
    proprietaire = models.CharField(max_length=50)
    image_support = models.ImageField(upload_to='collecte_images/', null=True, blank=True)
    duree=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    surface=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    TSP = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    ODP = models.BooleanField(default=False)  # Champ ODP
    ODP_value = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calculer le TSP en multipliant la surface par la durée
        self.TSP = self.surface * self.duree
        if self.ODP:
            self.ODP_value = self.surface * self.duree
        else:
            self.ODP_value = 0
        super(DonneeCollectee, self).save(*args, **kwargs)
    
    # Ajoutez d'autres champs pour les données collectées, comme des statistiques, etc.

    def __str__(self):
        return f"Donnée #{self.id} pour {self.support_publicitaire}"