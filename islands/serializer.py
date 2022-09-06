from rest_framework import serializers
from .models import Island


class IslandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'ocean', 'description', 'size', 'contributor')
        model = Island