from django.db import models

class Enterprise(models.Model):

    name = models.CharField(max_length=150)
    rut = models.CharField(max_length=12)
    giro = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name.split()[0]
    
