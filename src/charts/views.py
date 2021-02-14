from django.shortcuts import render
from rest_framework import generics
from .models import Chart
from .serializers import ChartSerializer


class ChartsList(generics.ListCreateAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer


class ChartDetail(generics.RetrieveDestroyAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer