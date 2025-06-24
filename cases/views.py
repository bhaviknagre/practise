from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import (
    Case, CaseStatus, CaseType, PaymentStatus,
    OpposingParty, Court, Judge
)
from .serializers import (
    CaseSerializer, CaseStatusSerializer, CaseTypeSerializer,
    PaymentStatusSerializer, OpposingPartySerializer,
    CourtSerializer, JudgeSerializer
)
from lawyer.models import LawyerProfile


# case vw 

class CaseListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cases = Case.objects.filter(lawyer__user=request.user)
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        try:
            data['lawyer'] = LawyerProfile.objects.get(user=request.user).id
        except LawyerProfile.DoesNotExist:
            return Response({'error': 'Lawyer profile not found.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CaseDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Case, pk=pk)

    def get(self, request, pk):
        case = self.get_object(pk)
        serializer = CaseSerializer(case)
        return Response(serializer.data)

    def put(self, request, pk):
        case = self.get_object(pk)
        data = request.data.copy()
        data.pop('lawyer', None)
        data.pop('client', None)
        serializer = CaseSerializer(case, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Case updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        case = self.get_object(pk)
        case.delete()
        return Response({'message': 'Case deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# crud operations

class GenericModelAPIView(APIView):
    permission_classes = [IsAuthenticated]
    model = None
    serializer_class = None

    def get(self, request):
        objects = self.model.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenericModelDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    model = None
    serializer_class = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# remining registrations views

class CaseStatusListCreateAPIView(GenericModelAPIView):
    model = CaseStatus
    serializer_class = CaseStatusSerializer

class CaseStatusDetailAPIView(GenericModelDetailAPIView):
    model = CaseStatus
    serializer_class = CaseStatusSerializer


class CaseTypeListCreateAPIView(GenericModelAPIView):
    model = CaseType
    serializer_class = CaseTypeSerializer

class CaseTypeDetailAPIView(GenericModelDetailAPIView):
    model = CaseType
    serializer_class = CaseTypeSerializer


class PaymentStatusListCreateAPIView(GenericModelAPIView):
    model = PaymentStatus
    serializer_class = PaymentStatusSerializer

class PaymentStatusDetailAPIView(GenericModelDetailAPIView):
    model = PaymentStatus
    serializer_class = PaymentStatusSerializer


class OpposingPartyListCreateAPIView(GenericModelAPIView):
    model = OpposingParty
    serializer_class = OpposingPartySerializer

class OpposingPartyDetailAPIView(GenericModelDetailAPIView):
    model = OpposingParty
    serializer_class = OpposingPartySerializer


class CourtListCreateAPIView(GenericModelAPIView):
    model = Court
    serializer_class = CourtSerializer

class CourtDetailAPIView(GenericModelDetailAPIView):
    model = Court
    serializer_class = CourtSerializer


class JudgeListCreateAPIView(GenericModelAPIView):
    model = Judge
    serializer_class = JudgeSerializer

class JudgeDetailAPIView(GenericModelDetailAPIView):
    model = Judge
    serializer_class = JudgeSerializer
