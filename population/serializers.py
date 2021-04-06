from rest_framework import serializers
from .models import Population

class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Population
        fields = ('id','url','dist_name','total','males','females')