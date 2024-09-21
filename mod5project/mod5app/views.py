from django.shortcuts import render
from mod5app.models import Appliance

# Create your views here.

def homePage(request):
    return render(request, 'index.html')

def viewAppliances(request):
    allApplicances = Appliance.objects.select_related('applianceManufacturer').all()
    return render(request, 'index.html', {'appliances' : allApplicances})