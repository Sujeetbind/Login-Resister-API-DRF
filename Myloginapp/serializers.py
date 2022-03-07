import email
from rest_framework import serializers
from .models import CustomUser,ApplicationId
from django.contrib.auth import authenticate

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username','email','mobile', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


class ApplicationIdSerializers(serializers.ModelSerializer):
     Full_name =serializers.CharField(max_length=100),
     Facebook_APP_ID = serializers.CharField(max_length=200),
     LinkedIn_APP_ID = serializers.CharField(max_length=200),
     Twitter_APP_ID = serializers.CharField(max_length=200),
     Intagram_APP_ID = serializers.CharField(max_length=200),

     class Meta:
        model = ApplicationId
        fields = ('Full_name','Facebook_APP_ID','LinkedIn_APP_ID','Twitter_APP_ID','Intagram_APP_ID')

        def create(self, validated_data):
           return ApplicationId.objects.create(**validated_data)