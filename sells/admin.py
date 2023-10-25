from django.contrib import admin

from .models import Sell, ItemSell, DocumentSellReference

admin.site.register(Sell)
admin.site.register(ItemSell)
admin.site.register(DocumentSellReference)
