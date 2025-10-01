from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
from .models import FlightRequest, Destination
from .serializers import FlightRequestSerializer, DestinationSerializer

# ViewSet para Destinos
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def list(self, request, *args, **kwargs):
        cached = cache.get('destinations')
        if cached:
            return Response(cached)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        cache.set('destinations', serializer.data, timeout=3600)  # 1 hora
        return Response(serializer.data)

# ViewSet para Solicitudes de Vuelo
class FlightRequestViewSet(viewsets.ModelViewSet):
    queryset = FlightRequest.objects.all()
    serializer_class = FlightRequestSerializer

    @action(detail=True, methods=['post'])
    def mark_reserved(self, request, pk=None):
        flight = self.get_object()
        flight.status = 'RESERVED'
        flight.save()
        return Response({'status': 'Flight marked as reserved'})
