from django.db import models


class FurnitureMovingModel(models.Model):
    HOME_TYPES = [
        ("Apartment", "Apartment"),
        ("Villa", "Villa"),
        ("Townhouse", "Townhouse"),
        ("Penthouse", "Penthouse"),
        ("Compound", "Compound"),
        ("Whole Building", "Whole Building"),
        ("Duplex", "Duplex"),
        ("Bulk Units", "Bulk Units"),
        ("Hotel Apartment", "Hotel Apartment"),
        ("Staff Accommodation", "Staff Accommodation"),
    ]

    FURNITURE_TYPES = [
        ("Bedroom", "Bedroom"),
        ("Bathroom", "Bathroom"),
        ("Balcony", "Balcony"),
        ("Dining Room", "Dining Room"),
        ("Hallway", "Hallway"),
        ("Home Office", "Home Office"),
        ("Kitchen", "Kitchen"),
        ("Living Room", "Living Room"),
        ("Garden", "Garden"),
        ("Gaming Room", "Gaming Room"),
    ]

    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)
    move_home = models.BooleanField()
    home_type = models.CharField(max_length=50, choices=HOME_TYPES, blank=True, null=True)
    request_visit = models.BooleanField(blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    visit_time = models.TimeField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    shipping_from = models.CharField(max_length=100)
    shipping_to = models.CharField(max_length=100)
    furniture_types = models.CharField(max_length=100, choices=FURNITURE_TYPES, blank=True, null=True)


class ShippingRequestModel(models.Model):
    COMMERCIAL_RETAIL_CHOICES = [
        ("Commercial", "Commercial"),
        ("Retail", "Retail"),
    ]

    VEHICLE_TYPES = [
        ("Car", "Car"),
        ("Motorbike", "Motorbike"),
        ("Pickup 2 Tons", "Pickup 2 Tons"),
        ("Pickup 4 Tons", "Pickup 4 Tons"),
        ("Van", "Van"),
    ]

    MATERIAL_TYPES = [
        ("Box", "Box"),
        ("Fragile", "Fragile"),
        ("Hazardous", "Hazardous"),
        ("Loose", "Loose"),
        ("Others", "Others"),
    ]

    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)
    commercial_retail = models.CharField(max_length=20, choices=COMMERCIAL_RETAIL_CHOICES)
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES, blank=True, null=True)
    material_type = models.CharField(max_length=50, choices=MATERIAL_TYPES)
    brief_description = models.CharField(max_length=255)
    pick_up_time = models.TimeField()
    image = models.CharField(max_length=255, blank=True, null=True)
    lifters_required = models.BooleanField()
    shipping_from = models.CharField(max_length=100)
    shipping_to = models.CharField(max_length=100)


class ConstructionRequestModel(models.Model):
    TRUCK_TYPES = [
        ("1 ton truck", "1 ton truck"),
        ("3 ton truck", "3 ton truck"),
        ("4.2 ton truck", "4.2 ton truck"),
        ("7 ton truck", "7 ton truck"),
        ("12 M truck", "12 M truck"),
        ("10 ton truck", "10 ton truck"),
        ("Trailer truck", "Trailer truck"),
        ("13.6 M truck", "13.6 M truck"),
        ("Tipper truck", "Tipper truck"),
        ("15 M truck", "15 M truck"),
    ]

    PACKING_TYPES = [
        ("Loose", "Loose"),
        ("Box", "Box"),
        ("Pallet", "Pallet"),
        ("Sacks", "Sacks"),
        ("Drums", "Drums"),
        ("Others", "Others"),
    ]

    truck_type = models.CharField(max_length=50, choices=TRUCK_TYPES)
    packing_type = models.CharField(max_length=50, choices=PACKING_TYPES)
    lifters_required = models.BooleanField()
    item_description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)


class PersonalShipmentModel(models.Model):
    VEHICLE_TYPES = [
        ("Car", "Car"),
        ("Motorbike", "Motorbike"),
        ("Pickup 2 Tons", "Pickup 2 Tons"),
        ("Pickup 4 Tons", "Pickup 4 Tons"),
        ("Van", "Van"),
    ]

    MATERIAL_TYPES = [
        ("Box", "Box"),
        ("Fragile", "Fragile"),
        ("Hazardous", "Hazardous"),
        ("Loose", "Loose"),
        ("Others", "Others"),
    ]

    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    material_type = models.CharField(max_length=50, choices=MATERIAL_TYPES)
    item_description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_type}"


class CrossBorderFreightModel(models.Model):
    MATERIAL_TYPES = [
        ("Box", "Box"),
        ("Fragile", "Fragile"),
        ("Hazardous", "Hazardous"),
        ("Loose", "Loose"),
        ("Others", "Others"),
    ]

    material_type = models.CharField(max_length=50, choices=MATERIAL_TYPES)
    length = models.FloatField(help_text="Length in meters")
    width = models.FloatField(help_text="Width in meters")
    height = models.FloatField(help_text="Height in meters")
    weight = models.FloatField(help_text="Weight in kg")
    lifters_required = models.BooleanField()
    image = models.CharField(max_length=255, blank=True, null=True)
    document = models.CharField(max_length=255, blank=True, null=True)
    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.material_type}"
