from django.db import models
from enterprises.models import Enterprise


class ItemCategory(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, null=True)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    base_price = models.IntegerField()
    unit = models.CharField(max_length=30)
    special_tax = models.IntegerField(default=1)
    internal_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name