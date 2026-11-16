from rest_framework import serializers
from .models import (
    Brand,
    Category,
    Product,
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
    parent_name = serializers.CharField(
        source = 'parent.name',
        read_only = True
    )
    
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
        
class ProductSerialzer(serializers.ModelSerializer):
    
    brand_name = serializers.CharField(
        source='brand.name',
        read_only=True
    )
    category_name = serializers.CharField(
       source='category.name',
       read_only=True 
    )
 
    final_price = serializers.SerializerMethodField()

    def get_final_price(self, obj):
        discount = obj.discount or 0
        discount_amount = obj.price * discount / 100
        return obj.price - discount_amount    
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'sku',
            'brand',
            'brand_name',
            'category',
            'category_name',
            'description',
            'price',
            'discount',
            'final_price',
            'status',
            'stock',
            'is_featured',
            'is_active',
            'created_at',
            'updated_at',
        ]
        
        read_only_fields = [
            'id',
            'slug', 
            'brand_name',
            'category_name',
            'final_price',
            'created_at',
            'updated_at',
            
        ]