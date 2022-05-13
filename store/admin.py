from django.contrib import admin
from .models import Stock
# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_name', 'category', )
    
    

admin.site.register(Stock, StockAdmin)