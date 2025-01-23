from rest_framework import serializers

from ride_app.models import Ride, RideEvent, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "phone_number",)


class RideEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideEvent
        fields = "__all__"


class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields = "__all__"


class RideListSerializer(serializers.ModelSerializer):
    id_rider = UserSerializer()
    id_driver = UserSerializer()
    todays_ride_events = RideEventSerializer(source="ride", many=True)
    distance = serializers.CharField(default="0")

    class Meta:
        model = Ride
        fields = (
            "id",
            "status",
            "id_rider",
            "id_driver",
            "pickup_latitude",
            "pickup_longitude",
            "dropoff_latitude",
            "dropoff_longitude",
            "pickup_time",
            "todays_ride_events",
            "distance",
            "created_at",
            "updated_at",
        )

