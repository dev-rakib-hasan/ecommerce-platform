from rest_framework import status
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