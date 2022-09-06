from django.shortcuts import render
from rest_framework import generics
from .serializer import IslandSerializer
from .models import Island
from .permissions import OwnershipRequired


class IslandList(generics.ListAPIView):
    permission_classes = (OwnershipRequired,)
    queryset = Island.objects.all()
    serializer_class = IslandSerializer


class IslandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (OwnershipRequired,)
    queryset = Island.objects.all()
    serializer_class = IslandSerializer

