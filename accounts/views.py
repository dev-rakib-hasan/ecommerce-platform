
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import(
    extend_schema,
    OpenApiParameter,
    OpenApiResponse, 
    OpenApiTypes,
)

from . models import(
    Brand,
    Category,
)

from . serializers import(
    Brandserializer,
    CategorySerializer,
)


# =============
# Brand Api
# =============
@extend_schema(
    tags=['Brand'],
    summary='List And Create Brand',
    description='Retrieve All Brand Or New Brand',
    request=Brandserializer,
    responses={
        200:Brandserializer(many=True),
        201:Brandserializer,
        400:OpenApiResponse(description='Validation error.'),
    }
    
)

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

@extend_schema(
    tags=['Brand'],
    summary='Retrieve, Update Or Delete Brand',
    description='Retrieve update or delete brand using ID.',
    parameters=[
        OpenApiParameter(
            name='pk',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.PATH,
            description='Brand Id'
            
        )
    ],
    request=Brandserializer,
    responses={
        200:Brandserializer,
        204:OpenApiResponse(description='Brand deleted successfully.'),
        400:OpenApiResponse(description='Validation errors.'),
        404:OpenApiResponse(description='Brand not found'),
    },
)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def brand_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
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
        return Response(status=status.HTTP_204_NO_CONTENT)


#=================
# Category API
#=================

@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(
            serializer.data
            )
    serializer = CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
        )
    
@extend_schema(
    tags=['Category'],
    summary='List And Create Category',
    description='Retrieve All Categories Or Add New Category',
    request=CategorySerializer,
    responses={
        200:CategorySerializer(many=True),
        201:CategorySerializer,
        400:OpenApiResponse(description='Validation error.'),
    }
    
)