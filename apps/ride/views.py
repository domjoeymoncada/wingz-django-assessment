from rest_framework import filters,viewsets
from apps.ride.models import Ride
from apps.ride.serializers import RideSerializer
from apps.ride.pagination import RidePagination
from django_filters.rest_framework import DjangoFilterBackend
from apps.ride.permissions import IsAdminRole
# Create your views here.
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.prefetch_related('events')
    serializer_class = RideSerializer
    pagination_class = RidePagination
    permission_classes = [IsAdminRole]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'rider__email']
    ordering_fields = ['pickup_time']
