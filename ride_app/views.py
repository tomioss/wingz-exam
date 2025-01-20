from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = (IsAuthenticated,)
    queryset = Ride.objects.all().order_by("id").select_related("id_rider", "id_driver").prefetch_related("ride")
    serializer_class = RideSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RideFilter

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
    permission_classes = (IsAuthenticated,)
    queryset = RideEvent.objects.all().order_by("id")
    serializer_class = RideEventSerializer

