from django.urls import path

from apps.roads.views import RoadView

urlpatterns = [
    path('', RoadView.as_view(), name='road'),
]
