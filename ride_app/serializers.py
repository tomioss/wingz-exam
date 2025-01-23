from rest_framework import serializers

from ride_app.models import Ride, RideEvent, User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name", "phone_number", "role")

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            role=validated_data["role"],
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "phone_number", "role")


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

