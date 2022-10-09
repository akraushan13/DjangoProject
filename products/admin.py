from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','created_at',)
    list_display_links = ('id','name',)
    list_filter = ('price',)
    search_fields = ('name','price',)
    ordering = ('price',)


admin.site.register(Product,ProductAdmin)