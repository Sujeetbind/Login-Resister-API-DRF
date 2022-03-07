from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken
from rest_framework.views import APIView
from .serializers import CreateUserSerializer, UserSerializer,ApplicationIdSerializers

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class AppIdViews(APIView):
    def post(self, request):
        serializer = ApplicationIdSerializers(data=request.data)
        if not serializer.is_valid():

            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
            