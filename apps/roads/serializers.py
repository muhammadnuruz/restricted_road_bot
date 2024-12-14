from rest_framework import serializers

from apps.roads.models import Roads


class RoadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roads
        fields = '__all__'
