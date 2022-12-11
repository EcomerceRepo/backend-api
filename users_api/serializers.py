from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('password', 'name', 'email', 'balance', 'joinDate', 'address', 'phoneNumber')
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }   
    def create(self, validatedData):
        print(validatedData)
        password = validatedData.pop('password', None)
        instance = self.Meta.model(**validatedData)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }   
    def create(self, validatedData):
        print(validatedData)
        password = validatedData.pop('password', None)
        instance = self.Meta.model(**validatedData)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

