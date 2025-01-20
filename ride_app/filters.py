from decimal import Decimal

from django_filters import rest_framework as filters

from ride_app.models import Ride


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
        position = [Decimal(v) for v in value.split(",")]
        return queryset

