from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from super_types.serializers import SuperTypeSerializer
from super_types.models import Super_Types
# Create your views here.

@api_view(['GET'])
def Super_types_list(request):
    super_types=Super_Types.objects.all()
    serializer = SuperTypeSerializer(super_types, many=True)
    return Response(serializer.data)

    