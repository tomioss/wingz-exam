from django.contrib import admin

from ride_app.models import Ride, RideEvent, User


class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("id", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined")
    search_fields = ("email",)


class RideAdmin(admin.ModelAdmin):
    model = Ride
    list_display = (
        "id",
        "status",
        "id_rider",
        "id_driver",
        "pickup_latitude",
        "pickup_longitude",
        "dropoff_latitude",
        "dropoff_longitude",
        "pickup_time",
        "created_at",
        "updated_at",
    )


class RideEventAdmin(admin.ModelAdmin):
    model = RideEvent
    list_display = (
        "id",
        "id_ride",
        "description",
        "created_at",
        "updated_at",
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Ride, RideAdmin)
admin.site.register(RideEvent, RideEventAdmin)

