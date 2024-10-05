from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import FurnitureMovingRequest, ShippingRequest, ConstructionRequest, PersonalShipmentRequest, \
    CrossBorderFreightRequest, VehicleBookingRequest

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Documentation",
        default_version='v1',
        description="API documentation for your Django project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('furniture-moving/', FurnitureMovingRequest.as_view(), name='furniture-moving'),
    path('shipping-request/', ShippingRequest.as_view(), name='shipping-request'),
    path('construction-request/', ConstructionRequest.as_view(), name='construction-request'),
    path('personal-shipment/', PersonalShipmentRequest.as_view(), name='personal-shipment-request'),
    path('cross-border-freight/', CrossBorderFreightRequest.as_view(), name='cross-border-freight-request'),
    path('vehicle-booking/', VehicleBookingRequest.as_view(), name='vehicle-booking'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
