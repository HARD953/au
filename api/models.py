# api/models.py
from django.dispatch import receiver
from django.db import models
from custumer.models import CustomUser
from django.db.models.signals import pre_save
from django.utils import timezone

class SupportPublicitaire(models.Model):
    type_support = models.CharField(max_length=50)
    surface= models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.type_support
    
class Taux(models.Model):
    TTAP = models.CharField(max_length=50)
    TTPAT= models.CharField(max_length=50)
    TAE = models.CharField(max_length=50)
    TAEAT = models.CharField(max_length=50)
    def __str__(self):
        return f"Donnée #{self.TTAP}_{self.TTPAT}_{self.TAE}_{self.TAEAT}"
    
class Marque(models.Model):
    marque = models.CharField(max_length=50)
    surface = models.CharField(max_length=50, blank=True)
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
    
class Ville(models.Model):
    ville = models.CharField(max_length=50,default="Abidjan")
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.ville

class Commune(models.Model):
    commune = models.CharField(max_length=50,default="Abidjan")
    tauxODP = models.CharField(max_length=50,default="6")
    tauxTSP=models.CharField(max_length=50,default="7")
    tauxAP = models.CharField(max_length=50)
    tauxAPA= models.CharField(max_length=50)
    tauxAPT = models.CharField(max_length=50)
    tauxAE = models.CharField(max_length=50)
    tauxAEA = models.CharField(max_length=50)
    tauxAET = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quartier(models.Model):
    commune = models.CharField(max_length=50,default="Abidjan")
    quartier= models.CharField(max_length=50,default="Rue 12")
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.quartier

# class Entreprise(models.Model):
#     agent=models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=1)
#     nom = models.CharField(max_length=50,default="Orange")
#     emplacement = models.CharField(max_length=50,default="6")
    def __str__(self):
        return self.commune

class DonneeCollectee(models.Model):
    agent=models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=1)
    entreprise = models.CharField(max_length=50, blank=True)
    Marque = models.CharField(max_length=50, blank=True)
    ville = models.CharField(max_length=50, blank=True)  # Utilise ForeignKey pour lier à la table Commune
    commune = models.CharField(max_length=50, blank=True)  # Utilise ForeignKey pour lier à la table Commune
    quartier = models.CharField(max_length=50, blank=True)
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
    anciennete = models.BooleanField(default=False, blank=True)
    TSP = models.CharField(max_length=50, default=12, blank=True)
    ODP = models.BooleanField(default=False, blank=True)
    AP = models.BooleanField(default=False, blank=True)
    APA = models.BooleanField(default=False, blank=True)
    APT = models.BooleanField(default=False, blank=True)
    AE = models.BooleanField(default=False, blank=True)
    AEA = models.BooleanField(default=False, blank=True)
    AET = models.BooleanField(default=False, blank=True)
    ODP_value = models.CharField(max_length=50, default=1, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)

    def save(self, *args, **kwargs):
        if not self.surface:
            # Si la surface est vide, récupérer la surface à partir du SupportPublicitaire
            try:
                support = SupportPublicitaire.objects.get(type_support=self.type_support)
                self.surface = support.surface
            except SupportPublicitaire.DoesNotExist:
                self.surface=0
        # Calculer TSP et ODP_value
        taux_commune = Commune.objects.get(commune=self.commune)
        self.tauxODP = taux_commune.tauxODP
        self.tauxAP = taux_commune.tauxAP
        self.tauxAPA = taux_commune.tauxAPA
        self.tauxAPT = taux_commune.tauxAPT
        self.tauxAE = taux_commune.tauxAE
        self.tauxAEA = taux_commune.tauxAEA
        self.tauxAET = taux_commune.tauxAET  
        if self.AP:
            self.TSP = float(self.surface) * float(self.duree) * float(self.tauxAP)
        elif self.APA:
            self.TSP = float(self.surface) * float(self.duree) * float(self.tauxAPA)
        elif self.APT:
            self.TSP = float(self.surface) * float(self.duree) * float(self.tauxAPT)
        elif self.AE:
            self.TSP = float(self.surface) * float(self.duree) * float(self.tauxAE)
        elif self.AEA:
            self.TSP = float(self.surface) * float(self.duree) * float(self.tauxAEA)
        elif self.AET:
            self.TSP = float(self.surface) * float(self.duree) * float(self.tauxAET)
        else: 
            self.TSP = float(self.surface) * float(self.duree)
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

    
