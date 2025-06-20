from django.shortcuts import render
from rest_framework import generics
from .models import Donation
from .serializers import DonationSerializer

# Create your views here.

class DonationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
