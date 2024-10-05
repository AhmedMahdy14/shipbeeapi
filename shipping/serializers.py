from rest_framework import serializers

from .models import FurnitureMovingModel, ShippingRequestModel, ConstructionRequestModel, PersonalShipmentModel, \
    CrossBorderFreightModel, VehicleBookingModel


class FurnitureMovingSerializer(serializers.ModelSerializer):
    home_type = serializers.ChoiceField(
        choices=[
            "Apartment", "Villa", "Townhouse", "Penthouse", "Compound",
            "Whole Building", "Duplex", "Bulk Units", "Hotel Apartment",
            "Staff Accommodation"
        ], required=False
    )
    furniture_types = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = FurnitureMovingModel
        fields = '__all__'
        extra_kwargs = {
            "name": {"required": True},
            "phone_number": {"required": True},
            "move_home": {"required": True},
            "shipping_from": {"required": True},
            "shipping_to": {"required": True},
            # Optional fields
            "email": {"required": False},
            "home_type": {"required": False},
            "visit_date": {"required": False},
            "visit_time": {"required": False},
            "address": {"required": False},
        }


class ShippingRequestSerializer(serializers.ModelSerializer):
    commercial_retail = serializers.ChoiceField(choices=["Commercial", "Retail"])
    vehicle_type = serializers.ChoiceField(
        choices=["Car", "Motorbike", "Pickup 2 Tons", "Pickup 4 Tons", "Van"], required=False
    )
    material_type = serializers.ChoiceField(
        choices=["Box", "Fragile", "Hazardous", "Loose", "Others"]
    )

    class Meta:
        model = ShippingRequestModel
        fields = '__all__'
        extra_kwargs = {
            "name": {"required": True},
            "phone_number": {"required": True},
            "commercial_retail": {"required": True},
            "material_type": {"required": True},
            # Optional fields
            "email": {"required": False},
            "vehicle_type": {"required": False},
            "image": {"required": False},
        }


class ConstructionRequestSerializer(serializers.ModelSerializer):
    truck_type = serializers.ChoiceField(choices=[
        "1 ton truck", "3 ton truck", "4.2 ton truck", "7 ton truck",
        "12 M truck", "10 ton truck", "Trailer truck", "13.6 M truck",
        "Tipper truck", "15 M truck"
    ])
    packing_type = serializers.ChoiceField(choices=[
        "Loose", "Box", "Pallet", "Sacks", "Drums", "Others"
    ])

    class Meta:
        model = ConstructionRequestModel
        fields = '__all__'
        extra_kwargs = {
            "name": {"required": True},
            "phone_number": {"required": True},
            "truck_type": {"required": True},
            # Specify which fields are optional
            "email": {"required": False},
            "image": {"required": False},
        }


class PersonalShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalShipmentModel
        fields = '__all__'
        extra_kwargs = {
            # Required fields
            "vehicle_type": {"required": True},
            "material_type": {"required": True},
            "item_description": {"required": True},
            "pickup_location": {"required": True},
            "drop_off_location": {"required": True},
            "name": {"required": True},
            "phone_number": {"required": True},
            # Optional fields
            "email": {"required": False},
            "image": {"required": False},
        }


class CrossBorderFreightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrossBorderFreightModel
        fields = '__all__'
        extra_kwargs = {
            # Required fields
            "material_type": {"required": True},
            "shipment_length": {"required": True},
            "shipment_width": {"required": True},
            "shipment_height": {"required": True},
            "weight": {"required": True},
            "pickup_location": {"required": True},
            "drop_off_location": {"required": True},
            "name": {"required": True},
            "phone_number": {"required": True},
            # Optional fields
            "email": {"required": False},
            "lifters_required": {"required": False},
            "image": {"required": False},
            "document": {"required": False},
        }


class VehicleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBookingModel
        fields = '__all__'
        extra_kwargs = {
            # Required fields
            "vehicle_type": {"required": True},
            "number_of_vehicles": {"required": True},
            "shipping_from": {"required": True},
            "shipping_to": {"required": True},
            "name": {"required": True},
            "phone_number": {"required": True},
            # Optional fields
            "email": {"required": False},
            "driver_required": {"required": False},
            "lifters_required": {"required": False},
            "item_description": {"required": False},
        }
