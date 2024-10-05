from rest_framework import serializers
from .models import FurnitureMovingModel, ShippingRequestModel, ConstructionRequestModel, PersonalShipmentModel, \
    CrossBorderFreightModel


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


class PersonalShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalShipmentModel
        fields = '__all__'


class CrossBorderFreightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrossBorderFreightModel
        fields = '__all__'
