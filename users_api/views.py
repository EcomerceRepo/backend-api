from rest_framework.decorators import api_view
from . import serializers
from rest_framework.response import Response

@api_view(['POST'])
def registerUser(request):
    clientSerializer = serializers.ClientSerializer(data=request.data)
    clientSerializer.is_valid(raise_exception=True)
    clientSerializer.save()
    return Response(clientSerializer.data)
