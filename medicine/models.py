from django.db import models

class medicine(models.Model):
    MedicineName =models.CharField(max_length=500)
    Description=models.TextField()
    ExpiryDate=models.DateField()
    Price=models.DecimalField(max_digits=10,decimal_places=2)
