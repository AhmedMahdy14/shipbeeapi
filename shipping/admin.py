from django.contrib import admin

from .models import (
    FurnitureMoving,
    ShippingRequest,
    ConstructionRequest,
    PersonalShipment,
    CrossBorderFreight, VehicleBooking, HomeType, FurnitureType, MaterialType, VehicleType
)


@admin.register(FurnitureMoving)
class FurnitureMovingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "move_home", "shipping_from", "shipping_to")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("move_home", "home_type", "furniture_types")


@admin.register(ShippingRequest)
class ShippingRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "is_commercial", "vehicle_type", "material_type")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("is_commercial", "vehicle_type", "material_type", "lifters_required")


@admin.register(ConstructionRequest)
class ConstructionRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "vehicle_type", "packing_type", "pickup_location", "drop_off_location")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("vehicle_type", "packing_type", "lifters_required")


@admin.register(PersonalShipment)
class PersonalShipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "vehicle_type", "material_type", "pickup_location", "drop_off_location")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("vehicle_type", "material_type")


@admin.register(CrossBorderFreight)
class CrossBorderFreightAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "material_type", "pickup_location", "drop_off_location", "weight")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("material_type", "lifters_required")


@admin.register(VehicleBooking)
class VehicleBookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "vehicle_type", "shipping_from", "shipping_to", "number_of_vehicle")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("vehicle_type", "driver_required", "lifters_required")


class BaseTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(HomeType)
class HomeTypeAdmin(BaseTypeAdmin):
    pass


@admin.register(FurnitureType)
class FurnitureTypeAdmin(BaseTypeAdmin):
    pass


@admin.register(MaterialType)
class MaterialTypeAdmin(BaseTypeAdmin):
    pass


@admin.register(VehicleType)
class VehicleTypeAdmin(BaseTypeAdmin):
    pass
