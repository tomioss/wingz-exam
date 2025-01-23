from decimal import Decimal, InvalidOperation

from django.db.models import Case, When, Value

from django_filters import rest_framework as filters

from haversine import haversine

from rest_framework.serializers import ValidationError

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
        error_msg = {"position": "parameter only accepts two numbers"}
        try:
            position = [Decimal(v) for v in value.split(",")]
        except InvalidOperation:
            raise ValidationError(error_msg)

        if len(position) != 2:
            raise ValidationError(error_msg)

        distances = []
        for loc in queryset:
            haversine_distance = haversine(position, (loc.pickup_latitude, loc.pickup_longitude))
            distances.append((loc.id, haversine_distance))

        distances.sort(key=lambda x: x[1])

        return queryset.annotate(
            distance=Case(*[When(pk=dist[0], then=Value(dist[1])) for dist in distances])
        ).order_by("distance")

