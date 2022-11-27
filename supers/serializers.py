from rest_framework import serializers
from supers.models import Supers
from super_types.models import Super_Types

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['name','alter_ego','primary_ability','secondary_ability','catchphrase','super_types',]
        depth = 1