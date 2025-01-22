from django.db.models import Prefetch
from django.utils import timezone

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from ride_app.filters import RideFilter
from ride_app.models import Ride, RideEvent
from ride_app.serializers import RideEventSerializer, RideListSerializer, RideSerializer


class RideApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAdminUser,)
    serializer_class = RideSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RideFilter

    def get_queryset(self):
        now = timezone.now()
        start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = now.replace(hour=23, minute=59, second=59, microsecond=999999)

        queryset = Ride.objects.all().order_by("id").select_related("id_rider", "id_driver").prefetch_related(
            Prefetch("ride", queryset=RideEvent.objects.filter(created_at__range=(start_date, end_date)))
        )
        return queryset


    def get_serializer_class(self):
        if self.action == "list":
            return RideListSerializer
        return RideSerializer


class RideEventApiView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAdminUser,)
    queryset = RideEvent.objects.all().order_by("id")
    serializer_class = RideEventSerializer

