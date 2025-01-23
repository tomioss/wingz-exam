from decimal import Decimal, InvalidOperation

from django_filters import rest_framework as filters

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

        return queryset

