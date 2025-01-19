from rest_framework import serializers

from ride_app.models import Ride, RideEvent, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone_number",)


class RideEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = RideEvent
        fields = "__all__"


class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields = "__all__"

