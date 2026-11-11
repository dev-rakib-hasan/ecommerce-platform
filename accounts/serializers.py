from rest_framework import serializers
from .models import (
    Brand,
)

class Brandserializer(serializers.ModelSerializer):
    class Meta:
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