from rest_framework import serializers
from .models import UsersModel,PatientAppointmentModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsersModel
        fields = '__all__'


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsersModel
        fields=['email','password','rol']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsersModel
        fields ='__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAppointmentModel
        fields = '__all__'
      