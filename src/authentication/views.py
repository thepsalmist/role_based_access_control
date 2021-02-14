from django.shortcuts import render
from rest_framework import generics, response, status
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response

# Create your views here.
class UserRegisterView(generics.GenericAPIView):
    """
    Registers user
    """

    serializer_class = UserRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        new_user = serializer.data

        return Response(new_user, status=status.HTTP_201_CREATED)


class UserLoginAPIView(generics.GenericAPIView):
    """
    Logins a registered user
    """

    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# class UserLogoutAPIView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer

#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request):

#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(status=status.HTTP_204_NO_CONTENT)