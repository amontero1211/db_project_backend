from rest_framework import viewsets, permissions
from .models import Artist, ArtWork, Invoice, Purchaser
from .serializers import ArtWorkSerializer, ArtistSerializer, InvoiceSerializer, PurchaserSerializer


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = ArtWork.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArtWorkSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArtistSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = InvoiceSerializer


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PurchaserSerializer
