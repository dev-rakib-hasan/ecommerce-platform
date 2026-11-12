from rest_framework import serializers
from .models import (
    Brand,
    Category,
)

class Brandserializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "is_active",
            "created_at",
            
        ]
        
        read_only_fields = [
            "id",
            "slug",
            "created_at",
        ]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'parent_name',
            'is_active',
            'created_at',
        ]
        
        read_only_fields = [
            'id',
            'slug',
            'parent_name',
            'created_at',
        ]