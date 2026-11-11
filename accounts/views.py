from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import(
    Brand,
)

from . serializers import(
    Brandserializer,
)


# =============
# Brand Api
# =============

@api_view(['GET', 'POST'])
def brand_list_create(request):
    if request.method == 'GET':
     brands = Brand.objects.all()
     serializer = Brandserializer(brands, many=True)
     return Response(
         serializer.data
     )
    
    serializer = Brandserializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def brand_detail(request, pk):
    brand = get_object_or_404(pk=pk)
#get method
    if request.method == 'GET':
        serializer = Brandserializer(brand)
        return Response(serializer.data)
    
#put patch method
    elif request.method in ['PUT','PATCH']:
        
        if request.method == 'PATCH':
            serializer = Brandserializer(
                brand,
                data=request.data,
                partial=True
                )
            
        else:
            serializer = Brandserializer(
                brand,
                data=request.data
                )
            
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        brand.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        