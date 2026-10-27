from rest_framework import filters,viewsets
from apps.ride.models import Ride, RideEvent
from apps.ride.serializers import RideSerializer
from apps.ride.pagination import RidePagination
from django_filters.rest_framework import DjangoFilterBackend
from apps.ride.permissions import IsAdminRole
from datetime import timedelta
from django.db.models import Prefetch
from django.utils import timezone

# Create your views here.
class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    pagination_class = RidePagination
    permission_classes = [IsAdminRole]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'rider__email']
    ordering_fields = ['pickup_time']

    def get_queryset(self):
        cutoff = timezone.now() - timedelta(hours=24)
        return (
            Ride.objects
            .prefetch_related(
                Prefetch(
                    'events',
                    queryset=RideEvent.objects.filter(created_at__gte=cutoff),
                    to_attr='todays_ride_events',
                )
            )
        )