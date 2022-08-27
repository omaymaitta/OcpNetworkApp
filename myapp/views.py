import site
from tkinter import E
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Contrat, Fournisseur, Site, Departement, Local, Equipement
from django.core.paginator import Paginator


def index(request):
  mysites = Site.objects.all().values()
  p = Paginator(Site.objects.all(),2)
  page = request.GET.get('page')
  sites = p.get_page(page)
  template = loader.get_template('siteview.html')
  context = {
    'mysites': mysites,
    'sites': sites,
  }
  return HttpResponse(template.render(context, request))

def departementview(request):
  mydeps = Departement.objects.all().values()
  mysites = Site.objects.all().values()
  p = Paginator(Departement.objects.all(),2)
  page = request.GET.get('page')
  deps = p.get_page(page)
  template = loader.get_template('departementview.html')
  context = {
    'deps': deps,
    'mydeps': mydeps,
    'mysites': mysites,
  }
  return HttpResponse(template.render(context, request))

def siteview(request):
  template = loader.get_template('siteview.html')
  return HttpResponse(template.render({}, request))

def dashboard(request):
  return HttpResponseRedirect(reverse('admin'))

def addrecordsite(request):
   x = request.POST['nameS']
   site = Site(nameS=x)
   site.save()
   return HttpResponseRedirect(reverse('index'))

def deletesite(request, id):
  site = Site.objects.get(id=id)
  site.delete()
  return HttpResponseRedirect(reverse('index'))

def updatesite(request, id):
  mysite = Site.objects.get(id=id)
  template = loader.get_template('updatesite.html')
  context = {
    'mysite': mysite,
  }
  return HttpResponse(template.render(context, request))

def updaterecordsite(request, id):
  name = request.POST['nameS']
  site = Site.objects.get(id=id)
  site.nameS = name
  site.save()
  return HttpResponseRedirect(reverse('index'))


def addrecorddep(request):
   x = request.POST['nameD']
   y = request.POST['namess']
   s = Site.objects.get(nameS=y)
   dep = Departement(nameD=x,site=s)
   dep.save()
   return HttpResponseRedirect(reverse('departementview'))

def deletedep(request, id):
    d = Departement.objects.get(id=id)
    d.delete()
    return HttpResponseRedirect(reverse('departementview'))

def updatedep(request, id):
    mydep = Departement.objects.get(id=id)
    mysites = Site.objects.all().values()
    template = loader.get_template('updatedep.html')
    context = {
    'mydep': mydep,
    'mysites': mysites,
  }
    return HttpResponse(template.render(context, request))

def updaterecorddep(request, id):
  name = request.POST['nameD']
  dep = Departement.objects.get(id=id)
  dep.nameD = name
  dep.save()
  return HttpResponseRedirect(reverse('departementview'))


def areaview(request):
  myareas = Local.objects.all().values()
  mydeps = Departement.objects.all().values()
  p = Paginator(Local.objects.all(),2)
  page = request.GET.get('page')
  areas = p.get_page(page)
  template = loader.get_template('areaview.html')
  context = {
    'areas': areas,
    'myareas': myareas,
    'mydeps': mydeps,
  }
  return HttpResponse(template.render(context, request))
def addrecordarea(request):
   x = request.POST['nameL']
   y = request.POST['named']
   yy = Departement.objects.get(nameD=y)
   l = Local(nameL=x, departement=yy)
   l.save()
   return HttpResponseRedirect(reverse('areaview'))

def deletearea(request, id):
    l = Local.objects.get(id=id)
    l.delete()
    return HttpResponseRedirect(reverse('areaview'))   
def updatearea(request, id):
    myarea = Local.objects.get(id=id)
    mydeps = Departement.objects.all().values()
    template = loader.get_template('updatearea.html')
    context = {
    'myarea': myarea,
    'mydeps': mydeps,
  }
    return HttpResponse(template.render(context, request))  

def updaterecordarea(request, id):
  name = request.POST['nameL']
  n = request.POST['named']
  l = Local.objects.get(id=id)
  d = Departement.objects.get(nameD=n)
  l.nameL = name
  l.departement = d
  l.save()
  return HttpResponseRedirect(reverse('areaview'))

def equipmentview(request):
  myeqs = Equipement.objects.all().values()
  myareas = Local.objects.all().values()
  p = Paginator(Equipement.objects.all(),2)
  page = request.GET.get('page')
  eqs = p.get_page(page)
  template = loader.get_template('equipmentview.html')
  context = {
    'eqs': eqs,
    'myeqs': myeqs,
    'myareas': myareas,
  }
  return HttpResponse(template.render(context, request))

def addrecordeq(request):
   a = request.POST['sn']
   b = request.POST['marque']
   c = request.POST['ip']
   d = request.POST['ismaintenu']
   e = request.POST['issupporte']
   f = request.POST['type']
   g = request.POST['local']
   h= Local.objects.get(nameL=g)
   l = Equipement(sn=a,marque=b,ip=c,ismaintenu=d,issupporte=e,type=f, local=h)
   l.save()
   return HttpResponseRedirect(reverse('equipmentview'))

def deleteeq(request, id):
    e = Equipement.objects.get(id=id)
    e.delete()
    return HttpResponseRedirect(reverse('equipmentview'))    
def updateeq(request, id):
    myeq= Equipement.objects.get(id=id)
    myareas = Local.objects.all().values()
    template = loader.get_template('updateeq.html')
    context = {
    'myeq': myeq,
    'myareas': myareas,
  }
    return HttpResponse(template.render(context, request))  

def updaterecordeq(request, id):
  a = request.POST['sn']
  b = request.POST['marque']
  c = request.POST['ip']
  d = request.POST['ismaintenu']
  e = request.POST['issupporte']
  f = request.POST['type']
  g = request.POST['local']
  h= Local.objects.get(nameL=g)
  eq = Equipement.objects.get(id=id)
  eq.sn = a
  eq.marque = b
  eq.ip = c
  eq.ismaintenu = d
  eq.issupporte = e
  eq.type = f
  eq.local = h
  eq.save()
  return HttpResponseRedirect(reverse('equipmentview'))


def contratview(request):
  mycs= Contrat.objects.all().values()
  myeqs= Equipement.objects.all().values()
  mypros = Fournisseur.objects.all().values()

  p = Paginator(Contrat.objects.all(),2)
  page = request.GET.get('page')
  cs = p.get_page(page)
  template = loader.get_template('contratview.html')
  context = {
    'cs': cs,
    'mycs': mycs,
    'myeqs': myeqs,
    'mypros': mypros,
  }
  return HttpResponse(template.render(context, request))  

def addrecordc(request):
   a = request.POST['date']
   b = request.POST['durre']
   c = request.POST['equipement']
   d = request.POST['provider']
   h= Equipement.objects.get(sn=c)
   g= Fournisseur.objects.get(nameF=d)
   l = Contrat(date=a,durre=b,equipement=h,fournisseur=g)
   l.save()
   return HttpResponseRedirect(reverse('contratview'))  

def deletec(request, id):
    e = Contrat.objects.get(id=id)
    e.delete()
    return HttpResponseRedirect(reverse('contratview'))    

def updatec(request, id):
    myc= Contrat.objects.get(id=id)
    myeqs= Equipement.objects.all().values()
    mypros = Fournisseur.objects.all().values()
    template = loader.get_template('updatec.html')
    context = {
    'myc': myc,
    'myeqs': myeqs,
    'mypros': mypros,
  }
    return HttpResponse(template.render(context, request))     

def updaterecordc(request, id):
   a = request.POST['date']
   b = request.POST['durre']
   c = request.POST['equipement']
   d = request.POST['fournisseur']
   h= Equipement.objects.get(sn=c)
   g= Fournisseur.objects.get(nameF=d)
   c = Contrat.objects.get(id=id)
   c.date=a
   c.durre=b
   c.equipement=h
   c.fournisseur=g 
   c.save()
   return HttpResponseRedirect(reverse('contratview'))

def providerview(request):
  mypros= Fournisseur.objects.all().values()
  p = Paginator(Fournisseur.objects.all(),2)
  page = request.GET.get('page')
  pros = p.get_page(page)
  template = loader.get_template('providerview.html')
  context = {
    'pros': pros,
    'mypros': mypros,
  }
  return HttpResponse(template.render(context, request))  

def addrecordpro(request):
   x = request.POST['nameF']
   f= Fournisseur(nameF=x)
   f.save()
   return HttpResponseRedirect(reverse('providerview'))  

def deletepro(request, id):
    l = Fournisseur.objects.get(id=id)
    l.delete()
    return HttpResponseRedirect(reverse('providerview'))   

def updatepro(request, id):
    mypro = Fournisseur.objects.get(id=id)
    template = loader.get_template('updatepro.html')
    context = {
    'mypro': mypro,
  }
    return HttpResponse(template.render(context, request))   

def updaterecordpro(request, id):
  name = request.POST['nameF']
  f = Fournisseur.objects.get(id=id)
  f.nameF = name
  f.save()
  return HttpResponseRedirect(reverse('providerview'))         
  