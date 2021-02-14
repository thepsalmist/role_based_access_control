from rest_framework import serializers
from .models import Chart


class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "author", "department", "published")
        model = Chart