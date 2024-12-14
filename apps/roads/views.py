from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.roads.models import Roads
from apps.roads.serializers import RoadsSerializer


class RoadView(generics.ListAPIView):
    queryset = Roads.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RoadsSerializer
