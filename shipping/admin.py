from django.contrib import admin
from .models import (
    FurnitureMovingModel,
    ShippingRequestModel,
    ConstructionRequestModel,
    PersonalShipmentModel,
    CrossBorderFreightModel
)


@admin.register(FurnitureMovingModel)
class FurnitureMovingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "move_home", "shipping_from", "shipping_to")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("move_home", "home_type", "furniture_types")


@admin.register(ShippingRequestModel)
class ShippingRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "commercial_retail", "vehicle_type", "material_type")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("commercial_retail", "vehicle_type", "material_type", "lifters_required")


@admin.register(ConstructionRequestModel)
class ConstructionRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "truck_type", "packing_type", "pickup_location", "drop_off_location")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("truck_type", "packing_type", "lifters_required")


@admin.register(PersonalShipmentModel)
class PersonalShipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "vehicle_type", "material_type", "pickup_location", "drop_off_location")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("vehicle_type", "material_type")


@admin.register(CrossBorderFreightModel)
class CrossBorderFreightAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "material_type", "pickup_location", "drop_off_location", "weight")
    search_fields = ("name", "phone_number", "email")
    list_filter = ("material_type", "lifters_required")
