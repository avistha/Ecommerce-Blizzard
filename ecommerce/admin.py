from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 4

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name','slug', 'total_products']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'is_available']
    list_editable = ['price', 'stock', 'is_available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInLine]

@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_display = ['name','email','phone', 'address']
    list_editable = ['email', 'phone', 'address'] 

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'city', 'total', 'status']
