from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import generics, permissions
from django.shortcuts import render

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]
    
class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]
    
def Index(request):
    return render(request, 'index.html')