from django.db import models

class Site(models.Model):
  nameS = models.CharField(max_length=255)
  def __str__(self):
        return self.nameS

class Departement(models.Model):
    nameD = models.CharField(max_length=255)
    site = models.ForeignKey(Site, null=True, on_delete= models.SET_NULL)
    def __str__(self):
        return self.nameD

class Local(models.Model):
    nameL = models.CharField(max_length=255)
    departement = models.ForeignKey(Departement, null=True, on_delete= models.SET_NULL)
    def __str__(self):
        return self.nameL

class Equipement(models.Model):
    sn = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    ismaintenu = models.BooleanField(default=False)
    issupporte = models.BooleanField(default=False)
    type = models.CharField(max_length=255)
    local = models.ForeignKey(Local, null=True, on_delete= models.SET_NULL)
    def __str__(self):
        return self.sn

class Fournisseur(models.Model):
    nameF = models.CharField(max_length=255)  
    def __str__(self):
        return self.nameF  
    
class Contrat(models.Model):
    date = models.DateField(auto_now_add=True)
    durre = models.CharField(max_length=255)
    equipement = models.ForeignKey(Equipement, null=True, on_delete= models.SET_NULL)
    fournisseur = models.ForeignKey(Fournisseur, null=True, on_delete= models.SET_NULL)



