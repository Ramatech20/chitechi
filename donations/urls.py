from django.urls import path
from donations.views import DonationListCreateAPIView

urlpatterns = [
    path('donations/', DonationListCreateAPIView.as_view(), name='donation-list-create'),
]
