from rest_framework import serializers
from things import models


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thing
