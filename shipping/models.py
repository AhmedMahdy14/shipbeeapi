from django.db import models

'''
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

    packing or MATERIAL TYPES = [
        ("Box", "Box"),
        ("Fragile", "Fragile"),
        ("Hazardous", "Hazardous"),
        ("Loose", "Loose"),
        ("Others", "Others"),
        ("Pallet", "Pallet"),
        ("Sacks", "Sacks"),
        ("Drums", "Drums"),
    ]
    
     vehicle   TRUCK_TYPES = [
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
        ("Car", "Car"),
        ("Motorbike", "Motorbike"),
        ("Pickup 2 Tons", "Pickup 2 Tons"),
        ("Pickup 4 Tons", "Pickup 4 Tons"),
        ("Van", "Van"),
    ]

    '''


class HomeType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class FurnitureType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class MaterialType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class FurnitureMoving(models.Model):
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)
    move_home = models.BooleanField()
    home_type = models.ForeignKey(HomeType, on_delete=models.SET_NULL, null=True, blank=True)
    request_visit = models.BooleanField(blank=True, null=True)
    visit_date = models.DateField(blank=True, null=True)
    visit_time = models.TimeField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    shipping_from = models.CharField(max_length=100)
    shipping_to = models.CharField(max_length=100)
    furniture_types = models.ForeignKey(FurnitureType, on_delete=models.SET_NULL, null=True, blank=True)


class ShippingRequest(models.Model):
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)
    is_commercial = models.BooleanField()  # if false, it's retail.
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True, blank=True)
    material_type = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True, blank=True)
    brief_description = models.CharField(max_length=255)
    pick_up_time = models.TimeField()
    image = models.CharField(max_length=255, blank=True, null=True)
    lifters_required = models.BooleanField()
    shipping_from = models.CharField(max_length=100)
    shipping_to = models.CharField(max_length=100)


class ConstructionRequest(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True, blank=True)
    packing_type = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True, blank=True)
    lifters_required = models.BooleanField()
    item_description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)


class PersonalShipment(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True, blank=True)
    material_type = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True, blank=True)
    item_description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_type}"


class CrossBorderFreight(models.Model):
    material_type = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True, blank=True)
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


class VehicleBooking(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_vehicle = models.PositiveIntegerField()
    driver_required = models.BooleanField()
    lifters_required = models.BooleanField()
    item_description = models.TextField()
    shipping_from = models.CharField(max_length=100)
    shipping_to = models.CharField(max_length=100)
    name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.name} - {self.vehicle_type}"
