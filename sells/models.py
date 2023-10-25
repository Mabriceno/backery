from django.db import models
from enterprises.models import Enterprise
from clients.models import Client
from dtes.models import DteType
from items.models import Item
#from inventories.models import Stock

class Sell(models.Model):

    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dte_type = models.ForeignKey(DteType, on_delete=models.CASCADE)
    folio = models.IntegerField()
    date = models.DateField()
    net_total = models.IntegerField()
    tax = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #when a sell is created, the stock of the items must be updated
    def save(self, *args, **kwargs):
        super(Sell, self).save(*args, **kwargs)
        items = ItemSell.objects.filter(sell=self)
        for item in items:
            item.item.stock -= item.quantity
            item.item.save()
    


class ItemSell(models.Model):

    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DocumentSellReference(models.Model):

    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    dte_type= models.ForeignKey(DteType, on_delete=models.CASCADE)
    folio = models.IntegerField()
    date = models.DateField()
    