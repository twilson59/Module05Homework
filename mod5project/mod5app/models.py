from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    manufacturerID = models.AutoField(primary_key=True)
    manufacturerName = models.CharField(max_length=50)
    manufacturerCountry = models.CharField(max_length=50)
    
    def __str__(self):
        return self.manufacturerName
        
    


class Appliance(models.Model):
    applianceID = models.AutoField(primary_key=True)
    applianceName = models.CharField(max_length=50)
    applianceNeedsElectric = models.BooleanField()
    applianceNeedsGas = models.BooleanField()
    applianceNeedsWater = models.BooleanField()
    applianceRoom = models.CharField(max_length=50)
    applianceManufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.applianceName
    