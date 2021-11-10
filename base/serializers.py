from .models import *
from rest_framework import serializers

class ExitPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExitPoint
        fields = ['name', 'tracking_difficulty_level', 'wingsuit_difficulty_level', 'rock_drop_second', 'rock_drop_altitude', 'landing_altitude']