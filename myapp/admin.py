from django.contrib import admin

from .models import Site, Departement, Equipement, Contrat, Fournisseur, Local
# Register your models here.

admin.site.register(Site)
admin.site.register(Departement)
admin.site.register(Equipement)
admin.site.register(Contrat)
admin.site.register(Fournisseur)
admin.site.register(Local)
admin.site.index_title = "Dashboard"
admin.site.site_title = "OCP Network"
admin.site.site_header= "OCP Network"
