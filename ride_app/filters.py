from decimal import Decimal, InvalidOperation

from django.db.models import F
from django.db.models.functions import Radians, Power, Sin, Cos, Sqrt, Radians, ASin

from django_filters import rest_framework as filters

from rest_framework.serializers import ValidationError

from ride_app.models import Ride


def haversine_distance(lat, long):
    rad_lat1 = Radians(F("pickup_latitude"))
    rad_long1 = Radians(F("pickup_longitude"))
    rad_lat2 = Radians(lat)
    rad_long2 = Radians(long)
    lat_diff = rad_lat1 - rad_lat2
    long_diff = rad_long1 - rad_long2

    a = (
        Power(Sin(lat_diff/2), 2) + Cos(rad_lat1) * Cos(rad_lat2) * Power(Sin(long_diff/2), 2)
    )

    c = 2 * ASin(Sqrt(a))

    # radius of earth in kilometers
    d = 6371 * c

    return d


class RideFilter(filters.FilterSet):
    rider_email = filters.CharFilter(field_name="id_rider__email", lookup_expr="exact")
    distance = filters.CharFilter(method="filter_distance")
    ordering = filters.OrderingFilter(
        fields=(
            ("pickup_time", "pickup_time"),
        ),
    )

    class Meta:
        model = Ride
        fields = (
            "status",
        )


    def filter_distance(self, queryset, name, value):
        # distance format: 'latitude,longitude'
        error_msg = {"position": "parameter only accepts two numbers"}
        try:
            position = [Decimal(v) for v in value.split(",")]
        except InvalidOperation:
            raise ValidationError(error_msg)

        if len(position) != 2:
            raise ValidationError(error_msg)

        return queryset.annotate(
            distance=haversine_distance(position[0], position[1])
        ).order_by("distance")

