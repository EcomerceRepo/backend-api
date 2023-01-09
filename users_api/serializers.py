from rest_framework import serializers
from . import models
from carts_api.models import Cart

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ["address", "phone_number"]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["department", "phone_number"]

class UserSerializer(serializers.ModelSerializer):
    client = ClientSerializer(required=False)
    employee = EmployeeSerializer(required=False)
    class Meta:
        model = models.User
        fields = ['id', 'email', 'password', 'client', 'employee', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        employee_data = validated_data.pop('employee', None)
        client_data = validated_data.pop('client', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        if instance.role == 1:
            models.Employee.objects.create(**employee_data, user=instance)
        else:
            models.Client.objects.create(**client_data, user=instance)
            Cart.objects.create(owner=instance)


        return instance
