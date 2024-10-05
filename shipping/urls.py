from django.urls import path
from .views import FurnitureMovingRequest, ShippingRequest, ConstructionRequest, PersonalShipmentRequest, \
    CrossBorderFreightRequest

urlpatterns = [
    path('furniture-moving/', FurnitureMovingRequest.as_view(), name='furniture-moving'),
    path('shipping-request/', ShippingRequest.as_view(), name='shipping-request'),
    path('construction-request/', ConstructionRequest.as_view(), name='construction-request'),
    path('personal-shipment/', PersonalShipmentRequest.as_view(), name='personal-shipment-request'),
    path('cross-border-freight/', CrossBorderFreightRequest.as_view(), name='cross-border-freight-request'),

]
