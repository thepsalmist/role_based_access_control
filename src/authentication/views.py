from django.shortcuts import render
from rest_framework import generics, response, status
from .serializers import RegisterSerializer
from rest_framework.response import Response

# Create your views here.
class UserRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        new_user = serializer.data

        return Response(new_user, status=status.HTTP_201_CREATED)