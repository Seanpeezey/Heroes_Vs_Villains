from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from supers.serializers import SuperSerializer
from supers.models import Supers
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        super_type = request.query_params.get('super_type_id')
        super=Supers.objects.all() 
        if super_type:
            super = super.filter(super_types_id=super_type)
        serializer = SuperSerializer(super, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def supers_details(request, pk):
    super = get_object_or_404(Supers, pk=pk)

    if request.method == 'GET':
        serializer = SuperSerializer(super);
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)