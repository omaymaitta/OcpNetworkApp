from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('siteview/', views.siteview, name='siteview'),
    path('siteview/addrecordsite/', views.addrecordsite, name='addrecordsite'),
    path('deletesite/<int:id>', views.deletesite, name='deletesite'),
    path('updatesite/<int:id>', views.updatesite, name='updatesites'),
    path('updatesite/updaterecordsite/<int:id>', views.updaterecordsite, name='updaterecordsite'),

    path('departementview/', views.departementview, name='departementview'),
    path('departementview/addrecorddep/', views.addrecorddep, name='addrecorddep'),
    path('departementview/deletedep/<int:id>', views.deletedep, name='deletedep'),
    path('departementview/updatedep/<int:id>', views.updatedep, name='updatedep'),
    path('departementview/updatedep/updaterecorddep/<int:id>', views.updaterecorddep, name='updaterecorddep'),

    path('areaview/', views.areaview, name='areaview'),
    path('areaview/addrecordarea/', views.addrecordarea, name='addrecordarea'),
    path('areaview/deletearea/<int:id>', views.deletearea, name='deletearea'),
    path('areaview/updatearea/<int:id>', views.updatearea, name='updatearea'),
    path('areaview/updatearea/updaterecordarea/<int:id>', views.updaterecordarea, name='updaterecordarea'),


    path('equipmentview/', views.equipmentview, name='equipmentview'),
    path('equipmentview/addrecordeq/', views.addrecordeq, name='addrecordeq'),
    path('equipmentview/deleteeq/<int:id>', views.deleteeq, name='deleteeq'),
    path('equipmentview/updateeq/<int:id>', views.updateeq, name='updateeq'),
    path('equipmentview/updateeq/updaterecordeq/<int:id>', views.updaterecordeq, name='updaterecordeq'),

    path('contratview/', views.contratview, name='contratview'),
    path('contratview/addrecordc/', views.addrecordc, name='addrecordc'),
    path('contratview/deletec/<int:id>', views.deletec, name='deletec'),
    path('contratview/updatec/<int:id>', views.updatec, name='updatec'),
    path('contratview/updatec/updaterecordc/<int:id>', views.updaterecordc, name='updaterecordc'),


    path('providerview/', views.providerview, name='providerview'),
    path('providerview/addrecordpro/', views.addrecordpro, name='addrecordpro'),
    path('providerview/deletepro/<int:id>', views.deletepro, name='deletepro'),
    path('providerview/updatepro/<int:id>', views.updatepro, name='updatepro'),
    path('providerview/updatepro/updaterecordpro/<int:id>', views.updaterecordpro, name='updaterecordpro'),




]