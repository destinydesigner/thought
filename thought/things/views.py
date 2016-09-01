from django.shortcuts import render
from rest_framework import viewsets
from things import models
from things import serializers

# Create your views here.
class ThingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Thing.objects.all()
    serializer_class = serializers.ThingSerializer
