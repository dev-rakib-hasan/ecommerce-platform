from django.contrib import admin
from .models import (
    Brand,
)

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'slug',
        'is_active',
        'created_at',
    ]
    
    list_search = [
        'is_active',
        'created_at',
    ]
    
    list_filter = [
        'name',
        'slug',    
    ]
    
    readonly_fields = [
        'slug',
        'created_at',
    ]
    ordering = ['name']
    #ordering = ['-created_at'] → নতুন Brand আগে দেখাবে।