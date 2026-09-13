from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.

api_view['POST']
def TransactionViewSet(request):
    serializer=TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response ('This is good')
    return Response('something went wrong over here')

