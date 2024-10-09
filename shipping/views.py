from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HomeType, FurnitureType, MaterialType, VehicleType
from .serializers import FurnitureMovingSerializer, ShippingRequestSerializer, ConstructionRequestSerializer, \
    VehicleBookingSerializer, HomeTypeSerializer, FurnitureTypeSerializer, MaterialTypeSerializer, VehicleTypeSerializer
from .serializers import PersonalShipmentSerializer, CrossBorderFreightSerializer


class HomeTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeType.objects.all()
    serializer_class = HomeTypeSerializer


# FurnitureType ViewSet
class FurnitureTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FurnitureType.objects.all()
    serializer_class = FurnitureTypeSerializer


# MaterialType ViewSet
class MaterialTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeSerializer


# VehicleType ViewSet
class VehicleTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class FurnitureMovingRequest(APIView):
    @swagger_auto_schema(
        request_body=FurnitureMovingSerializer,
        responses={201: "Furniture Moving Request received successfully", 400: "Validation Error"}
    )
    def post(self, request):
        serializer = FurnitureMovingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Furniture Moving Request received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShippingRequest(APIView):
    @swagger_auto_schema(
        request_body=ShippingRequestSerializer,
        responses={201: "Shipping Request received successfully", 400: "Validation Error"}
    )
    def post(self, request):
        serializer = ShippingRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Shipping Request received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConstructionRequest(APIView):
    @swagger_auto_schema(
        request_body=ConstructionRequestSerializer,
        responses={201: 'Construction Request received successfully', 400: 'Validation Error'}
    )
    def post(self, request):
        serializer = ConstructionRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Construction Request received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Personal Shipment View
class PersonalShipmentRequest(APIView):
    @swagger_auto_schema(
        request_body=PersonalShipmentSerializer,
        responses={201: "Personal Shipment Request received successfully", 400: "Validation Error"}
    )
    def post(self, request):
        serializer = PersonalShipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Personal Shipment request received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cross Border Freight View
class CrossBorderFreightRequest(APIView):
    @swagger_auto_schema(
        request_body=CrossBorderFreightSerializer,
        responses={201: "Cross Border Freight Request received successfully", 400: "Validation Error"}
    )
    def post(self, request):
        serializer = CrossBorderFreightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cross Border Freight request received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleBookingRequest(APIView):
    @swagger_auto_schema(
        request_body=VehicleBookingSerializer,
        responses={201: "Vehicle Booking Request received successfully", 400: "Validation Error"}
    )
    def post(self, request):
        serializer = VehicleBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Vehicle Booking received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
