from django.shortcuts import render
from rest_framework import generics
from .models import Chart
from .serializers import ChartSerializer
from rest_framework.permissions import IsAdminUser


class ChartsListView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer


class ChartDetail(generics.RetrieveDestroyAPIView):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer