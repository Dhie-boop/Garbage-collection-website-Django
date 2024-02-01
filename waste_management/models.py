from django.db import models

# Create your models here.
class create_bin(models.Model):
  
    LOADTYPE = (('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'))
    CYCLE_PERIOD = (('Daily', 'Daily'), ('Twice', 'Twice'), ('Weekly', 'Weekly'))
    area = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    street = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    assign_driver_email = models.EmailField(max_length=254, null=True)
    loadtype = models.CharField(max_length=20, null=True, choices=LOADTYPE)
    cycle_period = models.CharField(max_length=30, null=True, choices=CYCLE_PERIOD)
    best_route = models.CharField(max_length=240, null=True)
    
    def __str__(self):
        return self.area
    