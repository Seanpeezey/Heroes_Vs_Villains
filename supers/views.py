from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from super_types.serializers import SuperTypeSerializer
from supers.models import Supers


# Create your views here.

@api_view(['GET'])
def supers_list(request):
    supers=Supers.objects.all()
    serializer = SuperTypeSerializer(supers, many=True)
    return Response(serializer.data)