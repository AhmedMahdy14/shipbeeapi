from rest_framework.views import APIView
from .serializers import FurnitureMovingSerializer, ShippingRequestSerializer, ConstructionRequestSerializer


class FurnitureMovingRequest(APIView):
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
    def post(self, request):
        serializer = ConstructionRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Construction Request received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonalShipmentModel, CrossBorderFreightModel
from .serializers import PersonalShipmentSerializer, CrossBorderFreightSerializer


# Personal Shipment View
class PersonalShipmentRequest(APIView):
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
    def post(self, request):
        serializer = CrossBorderFreightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cross Border Freight request received successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
