from django.urls import path

from rest_framework.routers import DefaultRouter

from ride_app.views import CreateUserApiView, RideApiView, RideEventApiView


app_name = "ride_app"

router = DefaultRouter()
router.register("ride", RideApiView, basename="ride")
router.register("ride-event", RideEventApiView, basename="ride-event")

urlpatterns = router.urls + [
    path("create-user/", CreateUserApiView.as_view()),
]

