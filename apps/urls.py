from django.urls import path, include


urlpatterns = [
    path('roads/', include("apps.roads.urls")),
]
