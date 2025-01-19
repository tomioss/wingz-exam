from django.contrib import admin

from ride_app.models import User


class CustomUserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("id", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined")
    search_fields = ("email",)


admin.site.register(User, CustomUserAdmin)

