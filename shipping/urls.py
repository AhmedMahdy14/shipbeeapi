from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import FurnitureMovingRequest, ShippingRequest, ConstructionRequest, PersonalShipmentRequest, \
    CrossBorderFreightRequest, VehicleBookingRequest, VehicleTypeViewSet, MaterialTypeViewSet, FurnitureTypeViewSet, \
    HomeTypeViewSet

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

home_type_list = HomeTypeViewSet.as_view({
    'get': 'list'
})
home_type_detail = HomeTypeViewSet.as_view({
    'get': 'retrieve'
})

furniture_type_list = FurnitureTypeViewSet.as_view({
    'get': 'list'
})
furniture_type_detail = FurnitureTypeViewSet.as_view({
    'get': 'retrieve'
})

material_type_list = MaterialTypeViewSet.as_view({
    'get': 'list'
})
material_type_detail = MaterialTypeViewSet.as_view({
    'get': 'retrieve'
})

vehicle_type_list = VehicleTypeViewSet.as_view({
    'get': 'list'
})
vehicle_type_detail = VehicleTypeViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('home-types/', home_type_list, name='home-type-list'),
    path('home-types/<int:pk>/', home_type_detail, name='home-type-detail'),

    path('furniture-types/', furniture_type_list, name='furniture-type-list'),
    path('furniture-types/<int:pk>/', furniture_type_detail, name='furniture-type-detail'),

    path('material-types/', material_type_list, name='material-type-list'),
    path('material-types/<int:pk>/', material_type_detail, name='material-type-detail'),

    path('vehicle-types/', vehicle_type_list, name='vehicle-type-list'),
    path('vehicle-types/<int:pk>/', vehicle_type_detail, name='vehicle-type-detail'),

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
