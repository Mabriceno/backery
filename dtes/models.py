from django.db import models

class DteType(models.Model):
    name = models.CharField(max_length=150)
    code = models.IntegerField()
    update_inventary = models.BooleanField(default=False) 
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name