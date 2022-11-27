from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from supers.serializers import SuperSerializer
from supers.models import Supers


# Create your views here.

@api_view(['GET'])
def supers_list(request):
    supers=Supers.objects.all()
    serializer = SuperSerializer(supers, many=True)
    return Response(serializer.data)